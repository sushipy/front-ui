# coding: utf-8


class createHTML:

	def showlistHTML(self,countOB,eventlist):

		response = '<!DOCTYPE html>\n'
		response += '<html lang="ja">\n'
		response += '  <head>\n'
		response += '    <meta charset="utf-8">\n'
		response += '    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
		response += '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
		response += '    <script src="//oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>\n'
		response += '    <script src="//oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>\n'
		response += '    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">\n'
		response += '    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css" integrity="sha384-aUGj/X2zp5rLCbBxumKTCw2Z50WgIr1vs/PFN4praOTvYXWlVyh2UtNUU0KAUhAX" crossorigin="anonymous">\n'
		response += '    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>\n'
		response += '    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n'
		response += '    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>\n'
		response += '<style type="text/css" media="screen, projection">\n'
		response += 'html {\n'
		response += '  background: url(http://file.www.appkids.net/SBhrN.jpg) no-repeat center center fixed;\n'
		response += '  -webkit-background-size: cover;\n'
		response += '  -moz-background-size: cover;\n'
		response += '  -o-background-size: cover;\n'
		response += '  background-size: cover;\n'
		response += '}\n'
		response += '.row {\n'
		response += '  margin-top: auto;\n'
		response += '}\n'
		response += 'footer {\n'
		response += '    background-color: aliceblue;\n'
		response += '    text-align: center;\n'
		response += '    position: fixed;\n'
		response += '    bottom: 0;\n'
		response += '    width: 100%;\n'
		response += '    height: 20px;\n'
		response += '    bottom: 0;\n'
		response += '}\n'
		response += '</style>\n'
		response += '  </head>\n'
		response += '  <body>\n'
		response += '    <!-- ナビゲーションバー -->\n'
		response += '    <nav class="navbar navbar-default">\n'
		response += '      <div class="container-fluid">\n'
		response += '        <div class="nav-header">\n'
		response += '          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar">\n'
		response += '            <span class="sr-only">Toggle navbar</span>\n'
		response += '            <span class="icon-bar"></span>\n'
		response += '            <span class="icon-bar"></span>\n'
		response += '            <span class="icon-bar"></span>\n'
		response += '          </button>\n'
		response += '          <a class="navbar-brand" href="#">BMI22</a>\n'
		response += '        </div>\n'
		response += '        <div class="collapse navbar-collapse" id="navbar">\n'
		response += '         <button class="btn btn-default navbar-btn" data-toggle="modal" data-target="#createEvent">イベント作成</button>\n'
#		response += '         <button class="btn btn-default navbar-btn" data-toggle="modal" data-target="#deleteEvent">イベント削除</button>\n'
		response += '          <form class="navbar-form navbar-left" role="search">\n'
		response += '            <div class="form-group">\n'
		response += '              <input type="text" class="form-control" placeholder="未実装!!"/>\n'
		response += '            </div>\n'
		response += '            <button type="submit" class="btn btn-default"><span class="glyphicon glyphicon-search" aria-hidden="true"></span>検索</button>\n'
		response += '          </form>\n'
		response += '        </div>\n'
		response += '      </div>\n'
		response += '    </nav>\n'
		response += '    <!-- イベント新規作成 -->\n'
		response += '    <div class="modal fade" id="createEvent" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">\n'
		response += '      <div class="modal-dialog">\n'
		response += '        <div class="modal-content">\n'
		response += '          <div class="modal-header">\n'
		response += '            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n'
		response += '            <h4 class="modal-title" id="eventTitle">イベントを新規作成(＊は必須項目)</h4>\n'
		response += '          </div>\n'
		response += '          <div class="modal-body">\n'
		response += '            <form id="createForm">\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="title" class="control-label">イベント名 ＊</label>\n'
		response += '                <input type="text" class="form-control" id="eventTitle1" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="descri" class="control-label">詳細</label>\n'
		response += '                <textarea class="form-control" id="eventDescri" maxlength="50"></textarea>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="agenda" class="control-label">アジェンダ</label>\n'
		response += '                <textarea class="form-control" id="eventAgenda" maxlength="100"></textarea>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="note" class="control-label">連絡事項</label>\n'
		response += '                <input type="text" class="form-control" id="eventNote">\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="date" class="col-xs-2 control-label">開催日 ＊</label>\n'
		response += '                <input type="date" class="form-control" id="eventDate" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="stime" class="col-xs-2 control-label">開始時刻 ＊</label>\n'
		response += '                <input type="time" class="form-control" id="eventStime" step="900" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="ftime" class="col-xs-2 control-label">終了時刻 ＊</label>\n'
		response += '                <input type="time" class="form-control" id="eventFtime" step="900" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="room" class="control-label">開催場所 ＊</label>\n'
		response += '                <input type="text" class="form-control" id="eventRoom" placeholder="20F,C会議室@霞が関" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '               <label for="capacity" class="control-label">定員 ＊</label>\n'
		response += '               <input type="number" min="1" max="999" class="form-control" id="eventCapacity" placeholder="半角数字(1〜999)" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="promotor_name" class="control-label">主催者 ＊</label>\n'
		response += '                <input type="text" class="form-control" id="eventPromoName" placeholder="氏名" required>\n'
		response += '              </div>\n'
		response += '              <div class="form-group">\n'
		response += '                <label for="promotor_email" class="control-label" maxlength="30">主催者の連絡先 ＊</label>\n'
		response += '                <input type="email" class="form-control" id="eventPromoEmail" placeholder="メールアドレス" required>\n'
		response += '              </div>\n'
		response += '              <button type="submit" id="postFormInfo" class="btn btn-primary">作成</button>\n'
		response += '              <button type="submit" id="deleteFormInfo" class="btn btn-primary">削除</button>\n'
		response += '            </form>\n'
		response += '         </div>\n'
		response += '          <div class="modal-footer">\n'
		response += '            <button type="button" class="btn btn-default" data-dismiss="modal">閉じる</button>\n'
		response += '          </div>\n'
		response += '        </div>\n'
		response += '     </div>\n'
		response += '    </div>\n'
#		response += '    <!-- イベント削除 -->\n'
#		response += '    <div class="modal fade" id="deleteEvent" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">\n'
#		response += '      <div class="modal-dialog">\n'
#		response += '        <div class="modal-content">\n'
#		response += '          <div class="modal-header">\n'
#		response += '            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n'
#		response += '            <h4 class="modal-title" id="eventTitle">イベントを削除(＊は必須項目)</h4>\n'
#		response += '          </div>\n'
#		response += '          <div class="modal-body">\n'
#		response += '            <form id="deleteForm">\n'
#		response += '              <div class="form-group">\n'
#		response += '                <label for="title" class="control-label">主催者のメールアドレス</label>\n'
#		response += '                <input type="email" class="form-control" id="eventTitle" required>\n'
#		response += '              </div>\n'
#		response += '              <button type="submit" id="deleteFormInfo" class="btn btn-primary">削除</button>\n'
#		response += '            </form>\n'
#		response += '          </div>\n'
#		response += '          <div class="modal-footer">\n'
#		response += '           <button type="button" class="btn btn-default" data-dismiss="modal">閉じる</button>\n'
#		response += '         </div>\n'
#		response += '        </div>\n'
#		response += '      </div>\n'
#		response += '    </div>\n'
		response += '    <!-- top pate -->\n'

		#####################################################

		if countOB > 0:
			response += '    <div class="container-fluid">\n'
			response += '      <div class="row">\n'
			
			if countOB > 6:
				countOBi = 6
			else:
				countOBi = countOB

			ii=  1
			for cc in range(countOBi):
				response += '        <div class="col-xs-6 col-sm-4 col-md-2">\n'
				response += '          <h2>%s</h2>\n' % eventlist[countOB-ii]["title"]
				response += '          <h2>%s</h2>\n' % eventlist[countOB-ii]["date"]
				response += '          <p>%s</p>\n' % eventlist[countOB-ii]["descri"]
				response += '          <a class="btn btn-mini" href="/events/%s">&raquo; 詳細</a>\n' % eventlist[countOB-ii]["id"]
				response += '        </div>\n'
				ii += 1

		#####################################################

		response += '      </div>\n'
		response += '    </div>\n'
		response += '    <!-- javascript -->\n'
		response += '    <script type="text/javascript">\n'
		response += '$(function() {\n'
		response += '  $("#postFormInfo").click(function() {\n'
		response += '    // 多重送信を防ぐため通信完了までボタンをdisableにする\n'
		response += '    var button = $(this);\n'
		response += '    button.attr("disabled", true);\n'
		response += '    // 各フィールドから値を取得してJSONデータを作成\n'
		response += '    var data = {\n'
		response += '      title: $("#eventTitle1").val(),\n'
		response += '      descri: $("#eventDescri").val(),\n'
		response += '      agenda: $("#eventAgenda").val(),\n'
		response += '      note: $("#eventNote").val(),\n'
		response += '      date: $("#eventDate").val(),\n'
		response += '      time: $("#eventStime").val(),\n'
		response += '      ftime: $("#eventFtime").val(),\n'
		response += '      room: $("#eventRoom").val(),\n'
		response += '      capacity: $("#eventCapacity").val(),\n'
		response += '      promotor_name: $("#eventPromoName").val(),\n'
		response += '      promotor_email: $("#eventPromoEmail").val()\n'
		response += '    };\n'
		response += '    // 通信実行\n'
		response += '    $.ajax({\n'
		response += '      type: "post",\n'
		###response += '      url: "http://192.168.56.155:8001/create",\n'
		response += '      url: "http://10.194.23.240:8001/create",\n'
		response += '      data: JSON.stringify(data),\n'
		response += '      contentType: "application/json",\n'
		response += '      dataType: "json",\n'
		response += '      success: function(json_data) {\n'
		response += '        // 成功時処理\n'
		response += '        location.reload();\n'
		response += '      },\n'
		response += '      error: function() {\n'
		response += '        alert("Server Error. Pleasy try again later.");\n'
		response += '      },\n'
		response += '      complete: function() { //通信が終了した際の処理\n'
		response += '        button.attr("disabled", false);\n'
		response += '      },\n'
		response += '      timeout: 1000\n'
		response += '    });\n'
		response += '  });\n'
		response += '});\n'
#		response += '$(function() {\n'
#		response += '  $("#deleteFormInfo").click(function() {\n'
#		response += '    var button = $(this);\n'
#		response += '    button.attr("disabled", true);\n'
#		response += '    // 各フィールドから値を取得してJSONデータを作成\n'
#		response += '    var data = {\n'
#		response += '      event_id: $("#eventId").val(),\n'
#		response += '      promotor_email: $("#eventPromoEmail").val()\n'
#		response += '    };\n'
#		response += '    // 通信実行\n'
#		response += '    $.ajax({\n'
#		response += '      type: "delete",\n'
#		response += '      url: "http://192.168.56.155:8001/events/" + event_id,\n'
#		response += '      data: JSON.stringify(data),\n'
#		response += '      contentType: "application/json",\n'
#		response += '      dataType: "json",\n'
#		response += '      success: function(json_data) {\n'
#		response += '        if (!json_data[0]) {\n'
#		response += '          alert("Transaction error. " + json_data[1]);\n'
#		response += '          return;\n'
#		response += '        }\n'
#		response += '        // 成功時処理\n'
#		response += '        location.reload();\n'
#		response += '      },\n'
#		response += '      error: function() {\n'
#		response += '        alert("Server Error. Pleasy try again later.");\n'
#		response += '      },\n'
#		response += '      complete: function() { //通信が終了した際の処理\n'
#		response += '        button.attr("disabled", false);\n'
#		response += '      },\n'
#		response += '      timeout: 1000\n'
#		response += '    });\n'
#		response += '  });\n'
#		response += '});\n'
		response += '    </script>\n'
		response += '    <footer>\n'
		response += '      <div id="copyright">Copyright © 2015 ITOCHU Techno-Solutions Corporation All Right Reserved.</div>\n'
		response += '    </footer>\n'
		response += '  </body>\n'
		response += '</html>\n'

		return(response)

	def detailHTML(self,eventID,eventlist,partname):

		for tmpid in eventlist:
			if eventID == str(tmpid['id']):
				aaa = tmpid

				self.title1 = aaa['title']
				self.date1 = aaa['date']
				self.time1 = aaa['time']
				self.ftime1 = aaa['ftime']
				self.room1 = aaa['room']
				self.promotor_name1 = aaa['promotor_name']
				self.promotor_email1 = aaa['promotor_mail']
				self.descri = aaa['descri']
				self.agenda = aaa['agenda']
				self.note = aaa['note']

		response1 = '<!doctype html>\n'
		response1 += '<html lang="ja">\n'
		response1 += '  <head>\n'
		response1 += '    <meta charset="utf-8">\n'
		response1 += '    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
		response1 += '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
		response1 += '    <script src="//oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>\n'
		response1 += '    <script src="//oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>\n'
		response1 += '    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">'
		response1 += '    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css" integrity="sha384-aUGj/X2zp5rLCbBxumKTCw2Z50WgIr1vs/PFN4praOTvYXWlVyh2UtNUU0KAUhAX" crossorigin="anonymous">'
		response1 += '    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>\n'
		response1 += '    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n'
		response1 += '    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>\n'
		response1 += '<style type="text/css" media="screen, projection">\n'
		response1 += 'html {\n'
		response1 += '  background: url(http://file.www.appkids.net/SBhrN.jpg) no-repeat center center fixed;\n'
		response1 += '  -webkit-background-size: cover;\n'
		response1 += '  -moz-background-size: cover;\n'
		response1 += '  -o-background-size: cover;\n'
		response1 += '  background-size: cover;\n'
		response1 += '}\n'
		response1 += '.row {\n'
		response1 += '  margin-top: auto;\n'
		response1 += '}\n'
		response1 += 'footer {\n'
		response1 += '    background-color: aliceblue;\n'
		response1 += '    text-align: center;\n'
		response1 += '    position: fixed;\n'
		response1 += '    bottom: 0;\n'
		response1 += '    width: 100%;\n'
		response1 += '    height: 20px;\n'
		response1 += '    bottom: 0;\n'
		response1 += '}\n'
		response1 += '</style>\n'
		response1 += '  </head>\n'
		response1 += '  <body>\n'
		response1 += '    <div class="container">\n'
		response1 += '      <table class="table" id="descriTable">\n'
		response1 += '        <thread>\n'
		response1 += '          <tr>\n'
		response1 += '            <th>タイトル</th>\n'
		response1 += '            <th>日付</th>\n'
		response1 += '            <th>開始</th>\n'
		response1 += '            <th>終了</th>\n'
		response1 += '            <th>場所</th>\n'
		response1 += '            <th>主催者</th>\n'
		response1 += '            <th>主催者の連絡先</th>\n'
		response1 += '          </tr>\n'
		response1 += '        </thread>\n'
		response1 += '        <tbody>\n'
		response1 += '          <tr>\n'
		response1 += '            <td>%s</td>\n' % self.title1
		response1 += '            <td>%s</td>\n' % self.date1
		response1 += '            <td>%s</td>\n' % self.time1
		response1 += '            <td>%s</td>\n' % self.ftime1
		response1 += '            <td>%s</td>\n' % self.room1
		response1 += '            <td>%s</td>\n' % self.promotor_name1 
		response1 += '            <td>%s</td>\n' % self.promotor_email1
		response1 += '          </tr>\n'
		response1 += '        </tbody>\n'
		response1 += '      </table>\n'
		response1 += '      <div class="box">\n'
		response1 += '        <h3>内容</h3>\n'
		response1 += '        <p>%s</p>\n' % self.descri
		response1 += '        <h3>アジェンダ</h3>\n'
		response1 += '        <p>%s</p>\n' % self.agenda
		response1 += '        <h3>注意事項</h3>\n'
		response1 += '        <p>%s</p>\n' % self.note
		##############################################
		response1 += '        <h3>参加者</h3>\n'

		for dd in partname:
			print dd
			print dd['participant_name']
			response1 += '        <p>%s</p>\n' % dd['participant_name']
		#
		#
		#
		##############################################
		response1 += '        <button type="button" class="btn btn-default" data-toggle="modal" data-target="#joinEvent">参加</button>\n'
		response1 += '      </div>\n'
		response1 += '      <div class="modal" id="joinEvent" tabindex="-1" role="dialog" aria-labelledby="staticModalLabel" aria-hidden="true" data-show="true" data-keyboard="false" data-backdrop="static">\n'
		response1 += '        <div class="modal-dialog">\n'
		response1 += '          <div class="modal-content">\n'
		response1 += '            <div class="modal-header">\n'
		response1 += '              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n'
		response1 += '              <h3>あなたのメールアドレスを入力してください</h3>\n'
		response1 += '            </div>\n'
		response1 += '            <button type="button" class="close" data-dismiss="modal"></button>\n'
		response1 += '            <div class="modal-body">\n'
		response1 += '              <form id="joinEventForm">\n'
		response1 += '                <div class="form-group">\n'
		response1 += '                 <label for="title" class="control-label">メールアドレス</label>\n'
		response1 += '                 <input type="email" class="form-control" id="sendEmail" required>\n'
		response1 += '                </div>\n'
		response1 += '                  <div class="form-group">\n'
		response1 += '                    <input type="hidden" id="eventId" value="%s">\n' % eventID
		response1 += '                  </div>\n'
		response1 += '                <button type="submit" id="sendRegister" class="btn btn-primary">イベントへ参加</button>\n'
#		response1 += '                <button type="submit" id="sendUnRegister" class="btn">参加をキャンセル</button>\n'
		response1 += '                <input type="hidden" id="eventId" value="%s">\n' % eventID
		response1 += '              </form>\n'
		response1 += '            </div>\n'
		response1 += '          </div>\n'
		response1 += '        </div>\n'
		response1 += '      </div>\n'
		response1 += '    </div>\n'
		response1 += '    <!-- javascript -->\n'
		response1 += '    <script type="text/javascript">\n'
		response1 += '$(function() {\n'
		response1 += '  $("#sendRegister").click(function() {\n'
		response1 += '    // 多重送信を防ぐため通信完了までボタンをdisableにする\n'
		response1 += '    var button = $(this);\n'
		response1 += '    button.attr("disabled", true);\n'
		response1 += '    // 各フィールドから値を取得してJSONデータを作成\n'
		response1 += '    var data = {\n'
		response1 += '      promotor_email: $("#sendEmail").val(),\n'
		response1 += '      event_id: $("#eventId").val()\n'
		response1 += '    };\n'
		response1 += '    // 通信実行\n'
		response1 += '    $.ajax({\n'
		response1 += '      type: "post",\n'
		###response1 += '      url: "http://192.168.56.155:8001/events/%s",\n' %eventID
		response1 += '      url: "http://10.194.23.240:8001/events/%s",\n' %eventID
		response1 += '      data: JSON.stringify(data),\n'
		response1 += '      contentType: "application/json",\n'
		response1 += '      dataType: "json",\n'
		response1 += '      success: function(data) {\n'
#		response1 += '        if (!data[0]) {\n'
#		response1 += '          alert("Transaction error. " + data[1]);\n'
#		response1 += '          return;\n'
#		response1 += '        }\n'
		response1 += '        // 成功時処理\n'
		response1 += '        location.reload();\n'
		response1 += '      },\n'
		response1 += '      error: function() {\n'
		response1 += '        alert("Server Error. Pleasy try again later.");\n'
		response1 += '      },\n'
		response1 += '      complete: function() { //通信が終了した際の処理\n'
		response1 += '        button.attr("disabled", false);\n'
		response1 += '      },\n'
		response1 += '      timeout: 1000\n'
		response1 += '    });\n'
		response1 += '  });\n'
#		response1 += '  $("#sendUnRegister").click(function() {\n'
#		response1 += '    // 多重送信を防ぐため通信完了までボタンをdisableにする\n'
#		response1 += '    var button = $(this);\n'
#		response1 += '    button.attr("disabled", true);\n'
#		response1 += '    // 各フィールドから値を取得してJSONデータを作成\n'
#		response1 += '    var data = {\n'
#		response1 += '      promotor_email: $("#sendEmail").val(),\n'
#		response1 += '      evnet_id: $("#eventId").val()\n'
#		response1 += '    };\n'
#		response1 += '    // 通信実行\n'
#		response1 += '    $.ajax({\n'
#		response1 += '      type: "delete",\n'
#		response1 += '      url: "http://192.168.56.155:8001/events/" + eventId,\n'
#		response1 += '      data: JSON.stringify(data),\n'
#		response1 += '      contentType: "application/json",\n'
#		response1 += '      dataType: "json",\n'
#		response1 += '      success: function(json_data) {\n'
#		response1 += '        if (!json_data[0]) {\n'
#		response1 += '          alert("Transaction error. " + json_data[1]);\n'
#		response1 += '          return;\n'
#		response1 += '        }\n'
#		response1 += '        // 成功時処理\n'
#		response1 += '        location.reload();\n'
#		response1 += '      },\n'
#		response1 += '      error: function() {\n'
#		response1 += '        alert("Server Error. Pleasy try again later.");\n'
#		response1 += '      },\n'
#		response1 += '      complete: function() { //通信が終了した際の処理\n'
#		response1 += '        button.attr("disabled", false);\n'
#		response1 += '      },\n'
#		response1 += '      timeout: 1000\n'
#		response1 += '    });\n'
#		response1 += '  });\n'
		response1 += '});\n'
		response1 += '    </script>\n'
		response1 += '    <footer>\n'
		response1 += '      <div id="copyright">Copyright © 2015 ITOCHU Techno-Solutions Corporation All Right Reserved.</div>\n'
		response1 += '    </footer>\n'
		response1 += '  </body>\n'
		response1 += '</html>\n'

		return(response1)
