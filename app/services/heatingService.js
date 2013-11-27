var wiringpi = require( 'wiring-pi' );

var RELAY_A = 24
var RELAY_B = 25

exports.getCurrentState = function(){

  wiringpi.setup('gpio');

  var selectedRelay = RELAY_A
  var relayState = wiringpi.digitalRead(selectedRelay)
  return relayState;
};
