system = require('system')
address = system.args[1];//获得命令行第二个参数 接下来会用到     
var page = require('webpage').create();
var url = address;
phantom.outputEncoding = 'utf8';  
page.open(url, function (status) {  
    if (status !== 'success') {  
        console.log('Unable to post!');  
    } else {  
        console.log(page.content);//最后返回webkit加载之后的页面内容  
    }  
    phantom.exit();  
});
