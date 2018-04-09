/**
 * Created by superman on 26/11/2017.
 */
(function($){

    var createItem = function(roast){
        var d = roast['create_time'].replace("T", " ").replace("Z", "").strToDate();
        return $('\
            <div class="item">\
                <div class="left">\
                    <span class="day">{0}</span>\
                    <span class="month">{1}月</span>\
                </div>\
                <div class="right">\
                    <div class="talk">{2}</div>\
                </div>\
            </div>\
        '.format(d.getDate(), d.getMonth() + 1, roast['content']));
    };

    $('.roast-c .brush').on('click', function(){
        $(this).hide();
        $('.roast-c .publish').show();
    });

    $('.roast-c .publish-btn').on('click', function(){
        var content = $('.roast-c .roast-content').val();
        if($.trim(content) == ''){
            return ;
        }

        $.ajax({
            'url': '/roast/api_talk',
            'type': 'POST',
            'data': {
                'content': content
            },
            'success': function(){
                $('.roast-c .roast-content').val('');
                $('.roast-c .list .item-c').prepend(createItem({create_time: (new Date()).pattern(), content: content}));
            }
        });
    });

    $.ajax({
        'url': '/roast/api_get_list',
        'type': 'GET',
        'data': {

        },
        'success': function(result){
            var $c = $('.roast-c .list .item-c');
            for(var i = 0; i < result.roasts.length; i++){
                $c.append(createItem(result.roasts[i]));
            }
        }
    });

})(jQuery);