var ubit_ui = {
    
    init: function() {
        var html = '';
        html += '<link rel="stylesheet" href="static/css/mb.css"><div id="microbit">';
        html += '<div id="mb_btn_A" class="mb_btn"></div>';
        html += '<div id="mb_btn_B" class="mb_btn"></div>';
        
        var x,y;
        for(x = 0; x < 5; x++) {
            for(y = 0; y < 5; y++) {
                html += '<div class="mb_led mb_led_row_' + y + ' mb_led_col_' + x;
                html += '" id="mb_led_row_' + y + '.mb_led_col_' + x + '"></div>';
            }
        }
        
        var pinTp = '';
        for (var i = 0; i < 21; i++) {
            switch (i) {
                case 0: case 1: case 2:
                    pinTp = 'tch';
                    break;
                case 3: case 4: case 10:
                    pinTp = 'anlg';
                    break;
                default:
                    pinTp = 'dgtl';
                    break;
            }
            html += '<div id="mb_pin_' + i + '" class="mb_pin mb_pin_' + pinTp + '"></div>';
        }
        html += '</div>';
        document.getElementById("output").innerHTML += html;
    }
}