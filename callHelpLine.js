const accountSid = '';
const authToken = '';
const client = require('twilio')(accountSid, authToken);

function main(param){
    return new Promise(function(resolve, reject) {
    client.calls
      .create({
         url: 'http://demo.twilio.com/docs/voice.xml',
         to: param.toNumber,
         from: '+12048187600'
       })
      .then(call => resolve(call));
    })
}
