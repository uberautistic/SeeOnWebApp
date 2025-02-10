(function($){
    $.fn.extend({
        leanModal:function(options){
            var defaults = {top: 100, overlay: 0.5, closeButton: null};
            var overlay = $("<div id='lean_overlay'></div>");
            $("body").append(overlay);
            options = $.extend(defaults, options);
            return this.each(function(){
                var o = options;
                $(this).click(function(e){
                    var modal_id = $(this).attr("href");
                    $("#lean_overlay").click(function(){ close_modal(modal_id) });
                    $(o.closeButton).click(function(){ close_modal(modal_id) });
                    var modal_height = $(modal_id).outerHeight();
                    var modal_width = $(modal_id).outerWidth();
                    $("#lean_overlay").css({
                        "display": "flex",
                        "backdrop-filter": "blur(100px)",
                        "background-color": "rgba(0,0,0,0.6)",
                        "position": "fixed",
                        "flex-direction": "row",
                        "align-items": "center",
                        "top": 0,
                        "left": 0,
                        "width": "100%",
                        "height": "100%",
                        "z-index": 9999
                    });

                    $(modal_id).css({
                        "display": "block",
                        "position": "fixed",
                        "z-index": 11000,
                        "left": 50 + "%",
                        "margin-left": -(modal_width / 2) + "px",
                        "top": o.top + "px"
                    });
                    $("body").css("overflow", "hidden");
                    e.preventDefault();
                });
            });
            function close_modal(modal_id){
                $("#lean_overlay").css({"display": "none"});
                $(modal_id).css({"display": "none"});
                $("body").css("overflow", "auto");
            }
        }
    });
})(jQuery);

