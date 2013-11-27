var heatingService = require('../services/heatingService');
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { 
	  title: 'Express',
	  currentState: heatingService.getCurrentState()
  });
};