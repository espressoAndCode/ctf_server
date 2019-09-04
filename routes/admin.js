
const Joi = require("joi");
const passport = require("passport");
const router = require("express").Router();
const auth = require("./auth");
const generateJWT = require("../utils/generateJWT");

/* GET gamedata route */
router.get('/gamedata', (req, res) => {
  console.log('in the GET gamedata function');
  const data = '8:00:00 PM';

  // User.findAll().then(users => {
  //   return res.status(200).json(JSON.stringify(users));
  // });
  return res.status(200).json(JSON.stringify(data));
});

module.exports = router;
