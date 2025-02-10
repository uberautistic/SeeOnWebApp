$("#modal_trigger").leanModal({
		top: 100,
		closeButton: ".modal_close"
});
    $(".user_register").hide();
	$(".user_login").show();
$(function() {
		$("#login_form").click(function() {
				$(".user_register").hide();
				$(".user_login").show();
				return false;
		});

		$("#register_form").click(function() {
				$(".user_login").hide();
				$(".user_register").show();
			return false;
		});
});

