import json
import requests
import urllib.parse
import time
import datetime
import random
import os
import subprocess
from cache import cache


max_api_wait_time = 6
max_time = 4
apis = [
r"https://invidious.chunboan.zone/",
r"https://inv.us.projectsegfau.lt/",
r"https://inv.frail.duckdns.org/"
r"https://inv.pistasjis.net/",
r"https://inv.riverside.rocks/",
r"https://invidious.vern.cc/",
r"https://inv.us.projectsegfau.lt/",
r"https://inv.vern.cc/",
r"https://inv.zzls.xyz/",
r"https://invi.susurrando.com/",
r"https://yt.vern.cc/",
r"https://invidious.0011.lt/",
r"https://invidious.baczek.me/",
r"https://invidious.epicsite.xyz/",
r"https://invidious.esmailelbob.xyz/",
r"https://invidious.garudalinux.org/",
r"https://invidious.flokinet.to/",
r"https://invidious.kavin.rocks/",
r"https://invidious.lidarshield.cloud/",
r"https://invidious.lunar.icu/",
r"https://yt-us.discard.no/",
r"https://invidious.nerdvpn.de/",
r"https://invidious.privacydev.net/",
r"https://invidious.sethforprivacy.com/",
r"https://invidious.slipfox.xyz/",
r"https://yt-no.discard.no/",
r"https://invidious.snopyta.org/",
r"https://invidious.tiekoetter.com/",
r"https://invidious.vpsburti.com/",
r"https://invidious.weblibre.org/",
r"https://invidious.pufe.org/",
r"https://iv.ggtyler.dev/",
r"https://iv.melmac.space/",
r"https://vid.puffyan.us/",
r"https://watch.thekitty.zone/",
r"https://yt.yoc.ovh/",
r"https://y.com.sb/",
r"https://yewtu.be/",
r"https://youtube.moe.ngo/",
r"https://yt.artemislena.eu/",
r"https://yt.31337.one/",
r"https://yt.funami.tech/",
r"https://yt.oelrichsgarcia.de/",
r"https://yt.wkwkwk.fun/",
r"https://youtube.076.ne.jp/",
r"https://invidious.projectsegfau.lt/",
r"https://invidious.fdn.fr/",
r"https://i.oyster.men/",
r"https://invidious.domain.glass/",
r"https://inv.skrep.eu/",
r"https://clips.im.allmendenetz.de/", 
r"https://ytb.trom.tf/",
r"https://invidious.ethibox.fr/",
r"https://invidious.pcgamingfreaks.at/",
r"https://invidious.zapashcanon.fr/",
r"https://iteroni.com/",
r"https://invidious.grimneko.de/",
r"https://youtube.privacyplz.org/",
r"https://invidious.chunboan.zone/",
r"https://invidious.frbin.com/",
r"https://invidious.poast.org/",
r"https://iv.catgirl.cloud/",
r"https://subscriptions.gir.st/",
r"https://vro.omcat.info/",
r"https://video.weiler.rocks/",
r"https://yt.leverenz.email/",
r"https://yt.femboy.hu/",
r"https://monocles.live/",
r"https://youtube.it-service-schopfheim.de/",
r"https://invidious.longtime.duckdns.org/",
r"https://ytclient.antaresx.ch/",
r"https://youtube.noogle.gay/",
r"https://185.233.104.172/",
r.https://youtube.longtime.duckdns.org/",
r"https://aids.coronachan.tk/",
r"https://invidious.myachin.xyz/",
r"https://youtube.notrack.ch/",
r"https://iv.ok0.org/",
r"https://youtube.vpn-home-net.de/",
r"https://rust.oskamp.nl/",
r"http://144.126.251.186/",
r"https://invidious.citizen4.eu/",
r"https://yt.sebaorrego.net/",
r"https://invidious.pesso.al/",
r"https://invidious.manasiwibi.com/",
r"https://toob.unternet.org/",
r"https://youtube.mosesmang.com/",
r"https://invidious.varishangout.net/",
r"https://invidio.xamh.de/",
r"https://yt.tesaguri.club/",
r"https://invidious.qwik.space/",
r"https://video.francevpn.fr/",
r"https://inv.in.projectsegfau.lt/",
r"https://invid.nevaforget.de/",
r"https://tube.foss.wtf/",
r"https://invidious.777.tf/",
r"https://inv.tux.pizza/",
r"https://youtube.lurkmore.com/",
r"https://yt.artemislena.eu/",
r"https://youtube.076.ne.jp"m
r"https://invidious.osi.kr/",
r"https://invidious.flokinet.to/",
r"https://inv.riverside.rocks/",
r"https://inv.bp.mutahar.rocks/",
r"https://invidious.namazso.eu/",
r"https://tube.cthd.icu/",
r"https://invidious.snopyta.org/",
r"https://yewtu.be/",
r"https://invidious.privacy.gd/",
r"https://invidious.lunar.icu/",
r"https://vid.puffyan.us/",
r"https://invidious.weblibre.org/",
r"https://invidious.esmailelbob.xyz/",
r"https://invidio.xamh.de/",
r"https://invidious.kavin.rocks/",
r"https://invidious-us.kavin.rocks/",
r"https://invidious.mutahar.rocks/",
r"https://invidious.zee.li/",
r"https://tube.connect.cafe/",
r"https://invidious.zapashcanon.fr/",
r"https://invidious.poast.org/",
r"https://ytb.trom.tf/",
r"https://invidious.froth.zone/",
r"https://invidious.domain.glass/",
r"https://invidious.sp-codes.de/",
r"http://144.126.251.186/",
r"https://yt.512mb.org/",
r"https://invidious.ethibox.fr/",
r"https://invidious.fdn.fr/",
r"https://invidious.pcgamingfreaks.at/", 
r"https://tube.meowz.moe/",
r"https://clips.im.allmendenetz.de/",
r"https://inv.skrep.eu/",
r"https://invidious.frbin.com/",
r"https://dev.invidio.us/",
r"https://invidious.site/",
r"https://y.com.sb",
r"https://invidious.sethforprivacy.com/",
r"https://invidious.stemy.me/",
r"https://betamax.cybre.club/",
r"https://invidious.com/",
r"https://invidious.snopyta.org",
r"https://yewtu.be",
r"https://invidious.kavin.rocks",
r"https://vid.puffyan.us",
r"https://inv.riverside.rocks",
r"https://invidious.not.futbol/",
r"https://youtube.076.ne.jp",
r"https://yt.artemislena.eu",
r"https://invidious.flokinet.to",
r"https://invidious.esmailelbob.xyz",
r"https://invidious.projectsegfau.lt",
r"https://y.com.sb",
r"https://invidious.sethforprivacy.com",
r"https://invidious.tiekoetter.com",
r"https://invidious.nerdvpn.de",
r"https://invidious.slipfox.xyz",
r"https://inv.privacy.com.de",
r"https://invidious.rhyshl.live",
r"https://invidio.xamh.de",
r"https://invidious.dhusch.de",
r"https://inv.odyssey346.dev"
]
url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt').text.rstrip()
version = "1.0"

os.system("chmod 777 ./yukiverify")

apichannels = []
apicomments = []
[[apichannels.append(i),apicomments.append(i)] for i in apis]
class APItimeoutError(Exception):
    pass

def is_json(json_str):
    result = False
    try:
        json.loads(json_str)
        result = True
    except json.JSONDecodeError as jde:
        pass
    return result



def apicommentsrequest(url):
    global apicomments
    global max_time
    starttime = time.time()
    for api in apicomments:
        if  time.time() - starttime >= max_time -1:
            break
        try:
            res = requests.get(api+url,timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                return res.text
            else:
                print(f"エラー:{api}")
                apicomments.append(api)
                apicomments.remove(api)
        except:
            print(f"タイムアウト:{api}")
            apicomments.append(api)
            apicomments.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")

def apirequest(url):
    global apis
    global max_time
    starttime = time.time()
    for api in apis:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"成功したAPI: {api}")  
                return res.text
            else:
                print(f"エラー: {api}")
                apis.append(api)
                apis.remove(api)
        except:
            print(f"タイムアウト: {api}")
            apis.append(api)
            apis.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")

def apichannelrequest(url):
    global apichannels
    global max_time
    starttime = time.time()
    for api in apichannels:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"成功したAPI: {api}")  
                return res.text
            else:
                print(f"エラー: {api}")
                apichannels.append(api)
                apichannels.remove(api)
        except:
            print(f"タイムアウト: {api}")
            apichannels.append(api)
            apichannels.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")

def get_info(request):
    global version
    return json.dumps([version,os.environ.get('RENDER_EXTERNAL_URL'),str(request.scope["headers"]),str(request.scope['router'])[39:-2]])

def get_data(videoid):
    global logs
    t = json.loads(apirequest(r"api/v1/videos/"+ urllib.parse.quote(videoid)))
    return [{"id":i["videoId"],"title":i["title"],"authorId":i["authorId"],"author":i["author"]} for i in t["recommendedVideos"]],list(reversed([i["url"] for i in t["formatStreams"]]))[:2],t["descriptionHtml"].replace("\n","<br>"),t["title"],t["authorId"],t["author"],t["authorThumbnails"][-1]["url"]

def get_search(q,page):
    global logs
    t = json.loads(apirequest(fr"api/v1/search?q={urllib.parse.quote(q)}&page={page}&hl=jp"))
    def load_search(i):
        if i["type"] == "video":
            return {"title":i["title"],"id":i["videoId"],"authorId":i["authorId"],"author":i["author"],"length":str(datetime.timedelta(seconds=i["lengthSeconds"])),"published":i["publishedText"],"type":"video"}
        elif i["type"] == "playlist":
            return {"title":i["title"],"id":i["playlistId"],"thumbnail":i["videos"][0]["videoId"],"count":i["videoCount"],"type":"playlist"}
        else:
            if i["authorThumbnails"][-1]["url"].startswith("https"):
                return {"author":i["author"],"id":i["authorId"],"thumbnail":i["authorThumbnails"][-1]["url"],"type":"channel"}
            else:
                return {"author":i["author"],"id":i["authorId"],"thumbnail":r"https://"+i["authorThumbnails"][-1]["url"],"type":"channel"}
    return [load_search(i) for i in t]

def get_channel(channelid):
    global apichannels
    t = json.loads(apichannelrequest(r"api/v1/channels/"+ urllib.parse.quote(channelid)))
    if t["latestVideos"] == []:
        print("APIがチャンネルを返しませんでした")
        apichannels.append(apichannels[0])
        apichannels.remove(apichannels[0])
        raise APItimeoutError("APIがチャンネルを返しませんでした")
    return [[{"title":i["title"],"id":i["videoId"],"authorId":t["authorId"],"author":t["author"],"published":i["publishedText"],"type":"video"} for i in t["latestVideos"]],{"channelname":t["author"],"channelicon":t["authorThumbnails"][-1]["url"],"channelprofile":t["descriptionHtml"]}]

def get_playlist(listid,page):
    t = json.loads(apirequest(r"/api/v1/playlists/"+ urllib.parse.quote(listid)+"?page="+urllib.parse.quote(page)))["videos"]
    return [{"title":i["title"],"id":i["videoId"],"authorId":i["authorId"],"author":i["author"],"type":"video"} for i in t]

def get_comments(videoid):
    t = json.loads(apicommentsrequest(r"api/v1/comments/"+ urllib.parse.quote(videoid)+"?hl=jp"))["comments"]
    return [{"author":i["author"],"authoricon":i["authorThumbnails"][-1]["url"],"authorid":i["authorId"],"body":i["contentHtml"].replace("\n","<br>")} for i in t]

def get_replies(videoid,key):
    t = json.loads(apicommentsrequest(fr"api/v1/comments/{videoid}?hmac_key={key}&hl=jp&format=html"))["contentHtml"]

def get_level(yuki):
    for i1 in range(1,13):
        with open(f'Level{i1}.txt', 'r', encoding='UTF-8', newline='\n') as f:
            if siawaseok in [i2.rstrip("\r\n") for i2 in f.readlines()]:
                return i1
    return 0


def check_cokie(cookie):
    print(cookie)
    if cookie == "True":
        return True
    return False

def get_verifycode():
    try:
        result = subprocess.run(["./yukiverify"], encoding='utf-8', stdout=subprocess.PIPE)
        hashed_password = result.stdout.strip()
        return hashed_password
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None



from fastapi import FastAPI, Depends
from fastapi import Response, Cookie, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.responses import RedirectResponse as redirect
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Union


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/css", StaticFiles(directory="./css"), name="static")
app.mount("/word", StaticFiles(directory="./blog", html=True), name="static")
app.add_middleware(GZipMiddleware, minimum_size=1000)

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory='templates').TemplateResponse






@app.get("/", response_class=HTMLResponse)
def home(response: Response, request: Request, yuki: Union[str] = Cookie(None)):
    if check_cokie(yuki):
        response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
        return template("home.html", {"request": request})
    print(check_cokie(yuki))
    return redirect("/word")

@app.get('/watch', response_class=HTMLResponse)
def video(v:str, response: Response, request: Request, yuki: Union[str] = Cookie(None), proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie(key="yuki", value="True", max_age=7*24*60*60)
    videoid = v
    t = get_data(videoid)
    response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
    return template('video.html', {"request": request, "videoid":videoid, "videourls":t[1], "res":t[0], "description":t[2], "videotitle":t[3], "authorid":t[4], "authoricon":t[6], "author":t[5], "proxy":proxy})

@app.get("/search", response_class=HTMLResponse,)
def search(q:str, response: Response, request: Request, page:Union[int, None]=1, yuki: Union[str] = Cookie(None), proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
    return template("search.html", {"request": request, "results":get_search(q, page), "word":q, "next":f"/search?q={q}&page={page + 1}", "proxy":proxy})

@app.get("/hashtag/{tag}")
def search(tag:str, response: Response, request: Request, page:Union[int, None]=1, yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    return redirect(f"/search?q={tag}")


@app.get("/channel/{channelid}", response_class=HTMLResponse)
def channel(channelid:str, response: Response, request: Request, yuki: Union[str] = Cookie(None), proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
    t = get_channel(channelid)
    return template("channel.html", {"request": request, "results":t[0], "channelname":t[1]["channelname"], "channelicon":t[1]["channelicon"], "channelprofile":t[1]["channelprofile"], "proxy":proxy})

@app.get("/playlist", response_class=HTMLResponse)
def playlist(list:str, response: Response, request: Request, page:Union[int, None]=1, yuki: Union[str] = Cookie(None), proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
    return template("search.html", {"request": request, "results":get_playlist(list, str(page)), "word":"", "next":f"/playlist?list={list}", "proxy":proxy})

@app.get("/info", response_class=HTMLResponse)
def viewlist(response: Response, request: Request, yuki: Union[str] = Cookie(None)):
    global apis, apichannels, apicomments
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki", "True", max_age=60 * 60 * 24 * 7)
    return template("info.html", {"request": request, "Youtube_API":apis[0], "Channel_API":apichannels[0], "Comments_API":apicomments[0]})

@app.get("/suggest")
def suggest(keyword:str):
    return [i[0] for i in json.loads(requests.get(r"http://www.google.com/complete/search?client=youtube&hl=ja&ds=yt&q="+urllib.parse.quote(keyword)).text[19:-1])[1]]

@app.get("/comments")
def comments(request: Request, v:str):
    return template("comments.html", {"request": request, "comments":get_comments(v)})

@app.get("/thumbnail")
def thumbnail(v:str):
    return Response(content = requests.get(fr"https://img.youtube.com/vi/{v}/0.jpg").content, media_type=r"image/jpeg")

@app.get("/bbs",response_class=HTMLResponse)
def view_bbs(request: Request,name: Union[str, None] = "",seed:Union[str,None]="",channel:Union[str,None]="main",verify:Union[str,None]="false",yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    res = HTMLResponse(requests.get(fr"{url}bbs?name={urllib.parse.quote(name)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}",cookies={"yuki":"True"}).text)
    return res

@cache(seconds=5)
def bbsapi_cached(verify,channel):
    return requests.get(fr"{url}bbs/api?t={urllib.parse.quote(str(int(time.time()*1000)))}&verify={urllib.parse.quote(verify)}&channel={urllib.parse.quote(channel)}",cookies={"yuki":"True"}).text

@app.get("/bbs/api",response_class=HTMLResponse)
def view_bbs(request: Request,t: str,channel:Union[str,None]="main",verify: Union[str,None] = "false"):
    print(fr"{url}bbs/api?t={urllib.parse.quote(t)}&verify={urllib.parse.quote(verify)}&channel={urllib.parse.quote(channel)}")
    return bbsapi_cached(verify,channel)

@app.get("/bbs/result")
def write_bbs(request: Request,name: str = "",message: str = "",seed:Union[str,None] = "",channel:Union[str,None]="main",verify:Union[str,None]="false",yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    t = requests.get(fr"{url}bbs/result?name={urllib.parse.quote(name)}&message={urllib.parse.quote(message)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}&info={urllib.parse.quote(get_info(request))}&serververify={get_verifycode()}",cookies={"yuki":"True"}, allow_redirects=False)
    if t.status_code != 307:
        return HTMLResponse(t.text)
    return redirect(f"/bbs?name={urllib.parse.quote(name)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}")

@cache(seconds=30)
def how_cached():
    return requests.get(fr"{url}bbs/how").text

@app.get("/bbs/how",response_class=PlainTextResponse)
def view_commonds(request: Request,yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    return how_cached()

@app.get("/load_instance")
def home():
    global url
    url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt').text.rstrip()


@app.exception_handler(500)
def page(request: Request,__):
    return template("APIwait.html",{"request": request},status_code=500)

@app.exception_handler(APItimeoutError)
def APIwait(request: Request,exception: APItimeoutError):
    return template("APIwait.html",{"request": request},status_code=500)
