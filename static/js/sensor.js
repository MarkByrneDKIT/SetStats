var aliveSecond = 0;
var heartbeatRate = 5000;

var myChannel = "setstats-pi-channel"


var d = new Date();
var currentSec = d.getTime();

pubnub = new PubNub({
            publishKey : "pub-c-14d668cc-e874-4e1e-a4ab-bcf78c08744e",
            subscribeKey : "sub-c-76598f48-3f26-11ec-b886-526a8555c638",
            uuid: "590f83a0-2b19-4e7f-9cef-09882f022320"
        })

pubnub.addListener({
        status: function(statusEvent) {
            if (statusEvent.category === "PNConnectedCategory") {
                console.log("Successfully connected to Pubnub");
                publishSampleMessage();
            }
        },
        message: function(msg) {
            console.log(msg.message.title);
            console.log(msg.message.description);
        },

    })

pubnub.subscribe({channels: [myChannel]});

function publishUpdate(data, channel)
{
    pubnub.publish({
        channel: channel,
        message: data
        },
        function(status, response){
            if(status.error){
                console.log(status);
            }
            else
            {
                console.log("Message published with timetoken", response.timetoken)
            }
           }
        );
}


function handleClick(cb)
{
	if(cb.checked)
	{
		value = "ON";
	}
	else
	{
		value = "OFF";
	}
	var ckbStatus = new Object();
	ckbStatus[cb.id] = value;
	var event = new Object();
	event.event = ckbStatus;
	publishUpdate(event, myChannel);
}

