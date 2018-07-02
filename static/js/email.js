/**
 * Created by Administrator on 2018/6/23.
 */
$(document).ready(function () {
    //打开会员登录
    $("#Login_start_").click(function () {
        $("#regist_container").hide();
        $("#_close").show();
        $("#_start").animate({
            left: '350px',
            height: '520px',
            width: '400px'
        }, 500, function () {
            $("#login_container").show(500);
            $("#_close").animate({
                height: '40px',
                width: '40px'
            }, 500);
        });
    });
    //打开会员注册
    $("#Regist_start_").click(function () {
        $("#login_container").hide();
        $("#_close").show();
        $("#_start").animate({
            left: '350px',
            height: '520px',
            width: '400px'
        }, 500, function () {
            $("#regist_container").show(500);
            $("#_close").animate({
                height: '40px',
                width: '40px'
            }, 500);
        });
    });
    //关闭
    $("#_close").click(function () {

        $("#_close").animate({
            height: '0px',
            width: '0px'
        }, 500, function () {
            $("#_close").hide(500);
            $("#login_container").hide(500);
            $("#regist_container").hide(500);
            $("#_start").animate({
                left: '0px',
                height: '0px',
                width: '0px'
            }, 500);
        });
    });
    //去 注册
    $("#toRegist").click(function () {
        $("#login_container").hide(500);
        $("#regist_container").show(500);
    });
    //去 登录
    $("#toLogin").click(function () {
        $("#regist_container").hide(500);
        $("#login_container").show(500);
    });
});

/*<script type="text/javascript">
		var clock = '';
		var nums = 30;
		var btn;
		function sendCode(thisBtn) {
			btn = thisBtn;
			btn.disabled = true; //将按钮置为不可点击
			btn.value = '重新获取（'+nums+'）';
			clock = setInterval(doLoop, 1000); //一秒执行一次
		}

		function doLoop() {
			nums--;
			if (nums > 0) {
				btn.value = '重新获取（'+nums+'）';
			} else {
				clearInterval(clock); //清除js定时器
				btn.disabled = false;
				btn.value = '点击发送验证码';
				nums = 10; //重置时间
			}
		}

		$(document).ready(function(){
			$("#login_QQ").click(function(){
				alert("暂停使用！");
			});
			$("#login_WB").click(function(){
				alert("暂停使用！");
			});
		});
	</script>*/
