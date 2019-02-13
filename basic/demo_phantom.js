/*
console.log('Hello, world!');
phantom.exit();
*/

/*
// 获取页面并截图
var page = require('webpage').create();
page.open('https://aiui.iflyos.cn', function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.viewportSize = { width: 1366, height: 1500 };
        page.clipRect = { top: 0, left: 0, width: 1366, height: 1500 };
        page.render('example.png');
    }
    phantom.exit();
});
*/

/*
// 测试页面加载速度
var page = require('webpage').create(),
  system = require('system'),
  t, address;

if (system.args.length === 1) {
  console.log('Usage: loadspeed.js <some URL>');
  phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address, function(status) {
  if (status !== 'success') {
    console.log('FAIL to load the address');
  } else {
    t = Date.now() - t;
    console.log('Loading ' + system.args[1]);
    console.log('Loading time ' + t + ' msec');
  }
  phantom.exit();
});
// run: phantomjs demo_phantom.js https://aiui.iflyos.cn
*/

// 网络监听
var url = 'https://aiui.iflyos.cn';
var page = require('webpage').create();
page.onResourceRequested = function(request) {
  console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
  console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);

