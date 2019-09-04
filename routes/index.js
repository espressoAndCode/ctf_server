const express = require('express');
const router = express.Router();

router.use('/', require('./users'));
router.use('/admin', require('./admin'));
// router.use('/scoreboard', require('./scores'))

module.exports = router;
