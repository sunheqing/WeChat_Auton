# -*- coding: utf-8 -*-
#  filename: reply_xml.py
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
type=sys.getfilesystemencoding()

XmlForm_news = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
<CreateTime>{CreateTime}</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[{Content}]]></Title>
<Description><![CDATA[奥谭提供的新闻服务]]></Description>
<PicUrl><![CDATA[{PicUrl}]]></PicUrl>
<Url><![CDATA[{Url}]]></Url>
</item>
</Articles>
</xml>
"""

XmlForm_music = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
<CreateTime>{CreateTime}</CreateTime>
<MsgType><![CDATA[music]]></MsgType>
<Music>
<Title><![CDATA[奥谭-网易云音乐]]></Title>
<Description><![CDATA[Music]]></Description>
<MusicUrl><![CDATA[{Url}]]></MusicUrl>
<HQMusicUrl><![CDATA[{Url}]]></HQMusicUrl>
</Music>
<FuncFlag>0</FuncFlag></xml>"""

XmlForm_email = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
<CreateTime>{CreateTime}</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[{Content}]]></Title>
<Description><![CDATA[奥谭提供的邮件服务]]></Description>
<PicUrl><![CDATA[{PicUrl}]]></PicUrl>
<Url><![CDATA[{Url}]]></Url>
</item>
</Articles>
</xml>
"""

XmlForm_help = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
<CreateTime>{CreateTime}</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[{Content}]]></Title>
<Description><![CDATA[奥谭-操作手册]]></Description>
<PicUrl><![CDATA[{PicUrl}]]></PicUrl>
<Url><![CDATA[{Url}]]></Url>
</item>
</Articles>
</xml>
"""