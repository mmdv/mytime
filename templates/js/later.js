
jQuery(document).ready(function($) {
	$('#ok').click(function(){
		// 弹出输入层
		$('#inputBtn').fadeIn();
	});

	// 取消输入框
	$('#cancel').click(function(){
		$('#inputBtn').fadeOut()
	});
});