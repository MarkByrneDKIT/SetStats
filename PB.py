import os

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

ENTRY = "Earth"
CHANNEL = "setstats-pi-channel"
the_update = None

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-14d668cc-e874-4e1e-a4ab-bcf78c08744e"
pnconfig.subscribe_key = "sub-c-76598f48-3f26-11ec-b886-526a8555c638"
pnconfig.uuid = "590f83a0-2b19-4e7f-9cef-09882f022320"

pubnub = PubNub(pnconfig)


class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, event):
    print("[PRESENCE: {}]".format(event.event))
    print("uuid: {}, channel: {}".format(event.uuid, event.channel))

  def status(self, pubnub, event):
    if event.category == PNStatusCategory.PNConnectedCategory:
      print("[STATUS: PNConnectedCategory]")
      print("connected to channels: {}".format(event.affected_channels))

  def message(self, pubnub, event):
    print("[MESSAGE received]")

    if event.message["update"] == "42":
      print("The publisher has ended the session.")
      os._exit(0)
    else:
      print("{}: {}".format(event.message["entry"], event.message["update"]))

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(CHANNEL).with_presence().execute()

print("***************************************************")
print("* Waiting for updates to The Guide about {}... *".format(ENTRY))
print("***************************************************")

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, event):
      """handle presence events"""

    def status(self, pubnub, event):
      """handle status events"""

    def message(self, pubnub, event):
      """handle message events"""

pubnub.add_listener(MySubscribeCallback())

def message(self, pubnub, event):
  print("[MESSAGE received]")

  if event.message["update"] == "42":
    print("The publisher has ended the session.")
    os._exit(0)
  else:
    print("{}: {}".format(event.message["entry"], event.message["update"]))

def status(self, pubnub, event):
  if event.category == PNStatusCategory.PNConnectedCategory:
    print("[STATUS: PNConnectedCategory]")
    print("connected to channels: {}".format(event.affected_channels))
