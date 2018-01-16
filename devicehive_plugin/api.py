# Copyright (C) 2018 DataArt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


from devicehive_plugin.api_request import PluginRequest, TopicRequest


__all__ = ['Api']


class Api(object):
    def __init__(self, transport, access_token, topic_name):
        self._transport = transport
        self._access_token = access_token
        self._topic_name = topic_name
        self._connected = True

    @property
    def connected(self):
        return self._connected

    @property
    def transport(self):
        return self._transport

    def authenticate(self):
        request = PluginRequest(self)
        request.action('authenticate')
        request.set_payload('token', self._access_token)
        return request.execute()

    def subscribe(self):
        request = TopicRequest(self)
        request.action('subscribe')
        request.set_payload('t', [self._topic_name])
        return request.execute()

    def unsubscribe(self):
        request = TopicRequest(self)
        request.action('unsubscribe')
        request.set_payload('t', [self._topic_name])
        return request.execute()

    def disconnect(self):
        self._connected = False
        if not self._transport.connected:
            return
        self._transport.disconnect()
