var x = 0
var nextImage= function () {
x++;
                        if(x % 6 == 1){
                                $("#div1").append("<img id='1' img width='200' height='200' src='https://i1.sndcdn.com/avatars-000268413792-9vcaq9-t500x500.jpg'/>");
                                $("#div1").css('text-align','center');
                        }else if(x % 6 == 2){
                                $("#div1").append("<img id='2' img width='200' height='200' src='https://media.sanoma.fi/sites/default/files/styles/icon_lg/public/2018-03/IS.png?itok=UCxhUqwD'/>");
                        }else if(x % 6 == 3){
                                $("#div1").append("<img id='3' img width='200' height='200' src='https://upload.wikimedia.org/wikipedia/commons/1/15/Kanal_4_logo_Danmark.png'/>");
                        }else if(x % 6 == 4){
                                $("#div1").append("<img id='4' img width='200' height='200' src='https://ichef.bbci.co.uk/images/ic/1920x1080/p07hblcn.jpg'/>");
                        }else if (x % 6 == 5){
                                $("#div1").append("<img id='5' img width='200' height='200' src='https://cdn4.vectorstock.com/i/1000x1000/80/18/children-hand-written-word-text-for-typography-vector-21128018.jpg'/>");
                        }else{
                                x = 0;
                                $("#div1").empty()
                        }
                }
                setInterval(nextImage, 1000);
