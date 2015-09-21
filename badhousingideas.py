'''
Created on 21 Jun 2015

@author: @alexparsons

We have a shortage of housing, not bad housing ideas. Yet it is easier to train a robot to make these.
'''

import random
import twitter
import credentials

from classes import Robot, RobotMaster

random.seed()

words = ["Buy","Own","Rent","Let"]

verbs = ["is","are","has","get","see","need","know","would","find",
         "take","want","does","believe","learn","become","come",
         "include","thank","provide","create","add","understand",
         "consider","choose","develop","remember","determine",
         "grow","allow","supply","bring","improve","maintain","begin",
         "exist","tend","enjoy","perform","decide","identify",
         "continue","protect","require","occur","write","approach",
         "avoid","prepare","build","achieve","believe","receive",
         "seem","discuss","realize","contain","follow","refer",
         "solve","describe","prefer","prevent","discover",
         "ensure","expect","invest","reduce","speak","appear",
         "explain","explore","involve","lose","afford","agree",
         "hear","remain","represent","apply","forget",
         "recommend","rely","vary","generate","obtain",
         "accept","communicate","complain","depend",
         "enter","happen","indicate","suggest","survive",
         "appreciate","compare","imagine","manage","differ",
         "encourage","expand","prove","react","recognize","relax",
         "replace","borrow","earn","emphasize","enable","operate",
         "reflect","send","anticipate","assume","engage","enhance",
         "examine","install","participate","intend","introduce",
         "relate","settle","assure","attract","distribute","overcome",
         "owe","succeed","suffer","throw","acquire","adapt","adjust",
         "argue","arise","confirm","encouraging","incorporate",
         "justify","organize","ought","possess","relieve","retain",
         "shut","calculate","compete","consult","deliver","extend",
         "investigate","negotiate","qualify","retire","rid","weigh",
         "arrive","attach","behave","celebrate","convince","disagree",
         "establish","ignore","imply","insist","pursue","remaining","specify",
         "warn","accuse","admire","admit","adopt","announce","apologize","approve",
         "attend","belong","commit","criticize","deserve","destroy","hesitate",
         "illustrate","inform","manufacturing","persuade","pour","propose",
         "remind","shall","submit","suppose","translate","be","have","use",
         "make","look","help","go","being","think","read","keep","start",
         "give","play","feel","put","set","change","say","cut","show","try",
         "check","call","move","pay","let","increase","turn","ask","buy",
         "guard","hold","offer","travel","cook","dance","excuse","live",
         "purchase","deal","mean","fall","produce","search","spend","talk",
         "upset","tell","cost","drive","support","remove","return","run",
         "appropriate","reserve","leave","reach","rest","serve","watch",
         "charge","break","stay","visit","affect","cover","report","rise",
         "walk","pick","lift","mix","stop","teach","concern","fly","born",
         "gain","save","stand","fail","lead","listen","worry","express",
         "handle","meet","release","sell","finish","press","ride","spread",
         "spring","wait","display","flow","hit","shoot","touch","cancel","cry",
         "dump","push","select","conflict","die","eat","fill","jump","kick",
         "pass","pitch","treat","abuse","beat","burn","deposit","print",
         "raise","sleep","advance","connect","consist","contribute","draw",
         "fix","hire","join","kill","sit","tap","win","attack","claim","drag",
         "drink","guess","pull","wear","wonder","count","doubt","feed","impress",
         "repeat","seek","sing","slide","strip","wish","collect","combine","command",
         "dig","divide","hang","hunt","march","mention","smell","survey","tie",
         "escape","expose","gather","hate","repair","scratch","strike","employ",
         "hurt","laugh","lay","respond","split","strain","struggle","swim","train",
         "wash","waste","convert","crash","fold","grab","hide","miss","permit","quote",
         "recover","resolve","roll","sink","slip","suspect","swing","twist",
         "concentrate","estimate","prompt","refuse","regret","reveal","rush","shake",
         "shift","shine","steal","suck","surround","bear","dare","delay","hurry","invite",
         "kiss","marry","pop","pray","pretend","punch","quit","reply","resist","rip","rub",
         "smile","spell","stretch","tear","wake","wrap","was","like","even","film","water",
         "been","well","were","example","own","study","must","form","air","place","number",
         "part","field","fish","process","heat","hand","experience","job","book","end",
         "point","type","value","body","market","guide","interest","state","radio",
         "course","company","price","size","card","list","mind","trade","line",
         "care","group","risk","word","force","light","name","school","amount",
         "order","practice","research","sense","service","piece","web","boss","sport",
         "page","term","test","answer","sound","focus","matter","soil","board","oil",
         "picture","access","garden","open","range","rate","reason","according","site",
         "demand","exercise","image","case","cause","coast","age","boat","record","result",
         "section","building","mouse","cash","class","dry","plan","store","tax","involved",
         "side","space","rule","weather","figure","man","model","source","earth","program",
         "design","feature","purpose","question","rock","act","birth","dog",
         "object","scale","sun","fit","note","profit","related","rent","speed",
         "style","war","bank","content","craft","bus","exchange","eye","fire",
         "position","pressure","stress","advantage","benefit","box","complete",
         "frame","issue","limited","step","cycle","face","interested","metal",
         "paint","review","room","screen","structure","view","account","ball",
         "concerned","discipline","ready","share","balance","bit","black","bottom",
         "gift","impact","machine","shape","tool","wind","address","average",
         "career","culture","pot","sign","table","task","condition","contact",
         "credit","egg","hope","ice","network","separate","attempt","date",
         "effect","link","perfect","post","star","voice","challenge",
         "friend","warm","brush","couple","debate","exit","experienced",
         "function","lack","plant","spot","summer","taste","theme","track",
         "wing","brain","button","click","correct","desire","fixed","foot",
         "gas","influence","notice","rain","wall","base","damage","distance",
         "pair","staff","sugar","target","text","author","complicated","discount",
         "file","ground","lesson","officer","phase","reference","register","secure",
         "sky","stage","stick","title","trouble","advanced","bowl","bridge","campaign",
         "club","edge","evidence","fan","letter","lock","option","organized","pack","park",
         "quarter","skin","sort","weight","baby","carry","dish","exact","factor","fruit",
         "muscle","traffic","trip","appeal","chart","gear","land","log","lost","net",
         "season","spirit","tree","wave","belt","bench","closed","commission","copy",
         "drop","firm","frequent","progress","project","stuff","ticket","tour","angle",
         "blue","breakfast","doctor","dot","dream","essay","father","fee","finance",
         "juice","limit","luck","milk","mixed","mouth","pipe","please","seat","stable",
         "storm","team","amazing","bat","beach","blank","busy","catch","chain","cream",
         "crew","detail","detailed","interview","kid","mark","match","pain","pleasure",
         "score","screw","sex","sharp","shop","shower","suit","tone","window","wise",
         "band","block","bone","calendar","cap","coat","contest","court","cup",
         "district","finger","garage","guarantee","hole","hook","implement",
         "layer","lecture","lie","married","narrow","nose","partner","profile","respect",
         "rice","schedule","telephone","tip","bag","battle","bed","bill","bother","cake",
         "code","curve","dimension","ease","farm","fight","gap","grade","horse","host",
         "husband","loan","mistake","nail","noise","occasion","package","pause",
         "phrase","race","sand","sentence","shoulder","smoke","stomach","string"
         ,"surprise","towel","vacation","wheel","arm","associate",
         "bet","blow","border","branch","breast","buddy","bunch","chip",
         "coach","cross","document","draft","dust","floor","golf","habit",
         "iron","judge","knife","landscape","league","mail","mess","parent",
         "pattern","pin","pool","pound","request","salary","shame","shelter",
         "shoe","tackle","tank","trust","assist","bake","bar","bell","bike",
         "blame","brick","chair","closet","clue","collar","comment","conference",
         "devil","diet","fear","fuel","glove","jacket","lunch","monitor","mortgage",
         "nurse","pace","panic","peak","provided","reward","row","sandwich","shock",
         "spite","spray","surprise","till","transition","weekend","yard","alarm",
         "bend","bicycle","bite","blind","bottle","cable","candle","clerk","cloud",
         "concert","counter","dirty","flower","grandfather","harm","knee","lawyer",
         "load","loose","mirror","neck","pension","plate","pleased","proposed",
         "ruin","ship","skirt","slice","snow","stroke","switch","tired","trash",
         "tune","worried","zone","anger","award","bid","boot","bug","camp","candy",
         "carpet","cat","champion","channel","clock","comfort","cow","crack",
         "disappointed","empty","engineer","entrance","fault","grass","guy",
         "highlight","island","joke","jury","leg","lip","mate","nerve",
         "passage","pen","pride","priest","promise","resort","ring","roof",
         "rope","sail","scheme","script","slight","smart","sock",
         "station","toe","tower","truck","witness"]

formats = []
for w in words:
    formats.append("{0} to xxx".format(w))
    formats.append("xxx to {0}".format(w))

def generate():

    format = random.choice(formats)
    verb = random.choice(verbs)
    return format.replace("xxx",verb.title())
    
def tweet():

    api = twitter.Api(**credentials.twitter_badhousing)
    try:
        return api.PostUpdate(generate())
    except twitter.error.TwitterError,e:
        print e
housing = Robot("Bad Housing Ideas",tweet,minutes=85,uk_hours=True)

RobotMaster().register(housing)

if __name__ == "__main__":
    housing.tweet()