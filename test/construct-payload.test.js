/* eslint-env mocha */
const express = require('express');
const request = require('supertest');
const assert = require('assert');
const bodyParser = require('body-parser');

const constructPayload = require('../lib/construct-payload');

function createApp(options, existingPayload = { startedDateTime: new Date() }) {
  const app = express();
  app.use(bodyParser.json());
  app.post('/*', (req, res) => {
    res.json(constructPayload(req, res, () => {}, options, existingPayload));
  });

  return app;
}

describe('constructPayload()', () => {
  it('should construct a har file from the request/response', () =>
    request(createApp({ blacklist: ['password'] }))
      .post('/')
      .send({ password: '123456' })
      .expect(({ body }) => {
        assert.equal(typeof body.request.log.entries[0].request, 'object');
        assert.equal(typeof body.request.log.entries[0].response, 'object');
        assert(
          !body.request.log.entries[0].request.postData.text.match('password'),
          'Should pass through options',
        );
      }));

  it('#clientIPAddress', () =>
    request(createApp())
      .post('/')
      .expect(({ body }) => {
        assert.equal(body.clientIPAddress, '::ffff:127.0.0.1');
      }));

  it('#startedDateTime', () => {
    const startedDateTime = new Date();

    return request(createApp({}, { startedDateTime }))
      .post('/')
      .expect(({ body }) => {
        assert.equal(
          new Date(body.request.log.entries[0].startedDateTime).toISOString(),
          startedDateTime.toISOString(),
        );
      });
  });

  it('#time', () => {
    const startedDateTime = new Date();

    return request(createApp({}, { startedDateTime }))
      .post('/')
      .expect(({ body }) => {
        assert.equal(typeof body.request.log.entries[0].time, 'number');
        assert(body.request.log.entries[0].time > 0);
      });
  });
});