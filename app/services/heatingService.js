var wiringpi = require( 'node-wiringpi' );

var RELAY_A = 24
var RELAY_B = 25

exports.getCurrentState = function(){
  console.log( "you have " + wpi.num_pins() + " GPIO pins." );

  var selectedRelay = RELAY_A
  var relayState = wiringpi.digital_read(selectedRelay)
  return "ON!";
};