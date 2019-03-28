# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SessionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MG80af39294fe338b3848294685d097e04",
                "friendly_name": "friendly_name",
                "attributes": "{ \\"foo\\": \\"bar\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "created_by": "creator",
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "messages": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",
                    "webhooks": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions.create(messaging_service_sid="messaging_service_sid")

        values = {'MessagingServiceSid': "messaging_service_sid", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Sessions',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MG80af39294fe338b3848294685d097e04",
                "friendly_name": "friendly_name",
                "attributes": "{ \\"foo\\": \\"bar\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "created_by": "creator",
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "messages": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",
                    "webhooks": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions.create(messaging_service_sid="messaging_service_sid")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MG80af39294fe338b3848294685d097e04",
                "friendly_name": "friendly_name",
                "attributes": "{ \\"foo\\": \\"bar\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "created_by": "creator",
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "messages": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",
                    "webhooks": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Sessions',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sessions": [
                    {
                        "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "messaging_service_sid": "MG80af39294fe338b3848294685d097e04",
                        "friendly_name": "friendly_name",
                        "attributes": "{ \\"foo\\": \\"bar\\" }",
                        "date_created": "2015-12-16T22:18:37Z",
                        "date_updated": "2015-12-16T22:18:38Z",
                        "created_by": "creator",
                        "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "participants": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                            "messages": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",
                            "webhooks": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/Sessions?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://messaging.twilio.com/v1/Sessions?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "sessions"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions.list()

        self.assertIsNotNone(actual)
