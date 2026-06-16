#!/usr/bin/env python3
"""Build THE DARK ENLIGHTENMENT (DRK) — a TIN-FOIL-domain sphere on the real
neoreactionary (NRx) political philosophy, presented neutrally-but-critically and
NOT endorsed. Veracity verdict: REAL (a documented ideology with named authors and
primary texts — NOT the antisemitic Illuminati/NWO conspiracy it is sometimes
conflated with). Research-agent-verified; every critique attributed to a named
critic, not stated in the page's voice. Typographic hero + a VERACITY banner (the
Tin-Foil signature) on the standing full-bleed 3D backdrop."""
import os, html, base64, json, io, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

VERDICT = ("REAL", "#46c8e0", "a documented political philosophy — named authors, primary texts, traceable genealogy. Presented critically, NOT endorsed; and distinct from the antisemitic Illuminati/NWO conspiracy.")

REC = {
 "name": "THE DARK ENLIGHTENMENT", "axiom": "DRK",
 "position": "The Dark Enlightenment (neoreaction / NRx) — the real antidemocratic political philosophy of Curtis Yarvin & Nick Land",
 "origin": "an online antiliberal philosophy of the late-2000s tech milieu: the state as a corporation, democracy as a mistake, exit over voice",
 "mechanism": "Crystallized from the documented NRx corpus (Yarvin's Unqualified Reservations 2007-14; Land's essay 2012), research-agent-verified.",
 "crystallization": "The claim that the Enlightenment was a wrong turn: dissolve democracy, run the state as a gov-corp under a CEO-monarch, break the world into competing 'patches,' and replace voice with exit. A real ideology — and a critiqued one.",
 "nature": "The Dark Enlightenment — the neoreactionary philosophy of Yarvin and Land: the Cathedral, neocameralism, the patchwork, exit-over-voice, and the anti-democratic core, with the heavy weight of scholarly criticism represented as criticism.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Yarvin (Moldbug); Nick Land; the Cathedral; neocameralism; the patchwork; exit over voice; RAGE; accelerationism",
 "witness": "A real, citable ideology — not a conspiracy theory. Its author calls the Cathedral emergent, not a cabal; critics call that a distinction without a difference. The page keeps both.",
 "role": "the neoreaction sphere (real ideology, examined)",
 "seal": "It says the Enlightenment was the error and democracy the failure mode — written down, by name, in primary texts. You do not have to believe it to read it honestly, and you should not mistake it for the cabal myth next door.",
 "source": "the NRx corpus, catalogued by ROOT0",
}
NATURES = {
 "natural":   ("#d89030", "the people — Yarvin, Land, the tech milieu, and the named critics"),
 "ethereal":  ("#9aa6bc", "the concepts — the Cathedral, exit-over-voice, the anti-Enlightenment thesis"),
 "spiritual": ("#c060f0", "the core claim and the honest line — &lsquo;the Enlightenment was a mistake,&rsquo; and why this is NOT the Illuminati"),
 "electrical":("#46c8e0", "the machinery — neocameralism / gov-corp, the patchwork, RAGE, accelerationism"),
}

BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');var W,H,CX,CY,F,R;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.46;F=Math.max(440,W*0.62);R=Math.min(W,H)*0.36;}
window.addEventListener('resize',resize);resize();
var rnd=(function(){var s=4044;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
var N=42,nodes=[];for(var i=0;i<N;i++){var u=rnd()*2-1,th=rnd()*6.283,sq=Math.sqrt(1-u*u),r=Math.cbrt(rnd());nodes.push([r*sq*Math.cos(th),r*sq*Math.sin(th),r*u,rnd()]);}
var edges=[];for(var a=0;a<N;a++){var ds=[];for(var b=0;b<N;b++){if(b===a)continue;var dx=nodes[a][0]-nodes[b][0],dy=nodes[a][1]-nodes[b][1],dz=nodes[a][2]-nodes[b][2];ds.push([dx*dx+dy*dy+dz*dz,b]);}ds.sort(function(p,q){return p[0]-q[0]});for(var k=0;k<2;k++)if(ds[k][1]>a)edges.push([a,ds[k][1]]);}
function rotY(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0]*co+p[2]*s,p[1],-p[0]*s+p[2]*co];}
function rotX(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0],p[1]*co-p[2]*s,p[1]*s+p[2]*co];}
function proj(p){var z=p[2]*R+F+R*0.2;if(z<1)z=1;return[CX+p[0]*R*F/z,CY+p[1]*R*F/z,z];}
function frame(t){
 var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#06070a');sg.addColorStop(0.6,'#090a10');sg.addColorStop(1,'#040406');x.fillStyle=sg;x.fillRect(0,0,W,H);
 x.globalCompositeOperation='lighter';var cg=x.createRadialGradient(CX,CY,0,CX,CY,R*1.6);cg.addColorStop(0,'rgba(154,166,188,0.05)');cg.addColorStop(1,'rgba(154,166,188,0)');x.fillStyle=cg;x.fillRect(0,0,W,H);x.globalCompositeOperation='source-over';
 var ang=t/10000,tilt=0.3+Math.sin(t/13000)*0.05,P=[];for(var i=0;i<N;i++)P.push(proj(rotX(rotY(nodes[i],ang),tilt)));
 x.globalCompositeOperation='lighter';
 for(var e=0;e<edges.length;e++){var A=P[edges[e][0]],B=P[edges[e][1]];var dep=1-Math.min(1,((A[2]+B[2])/2-F)/(R*1.4));x.strokeStyle='rgba(140,150,170,'+(0.04+0.11*dep)+')';x.lineWidth=0.5;x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.stroke();}
 var o=[];for(var n2=0;n2<N;n2++)o.push(n2);o.sort(function(a,b){return P[b][2]-P[a][2];});
 for(var k=0;k<o.length;k++){var ni=o[k],pp=P[ni],dp=1-Math.min(1,(pp[2]-F)/(R*1.6));var warm=nodes[ni][3]<0.22;
  x.save();x.shadowColor=warm?'rgba(216,144,48,1)':'rgba(150,162,188,1)';x.shadowBlur=8*dp+2;x.fillStyle=warm?'rgba(224,160,70,'+(0.3+0.6*dp)+')':'rgba(160,172,196,'+(0.25+0.55*dp)+')';x.beginPath();x.arc(pp[0],pp[1],1.3+2.7*dp,0,7);x.fill();x.restore();}
 x.globalCompositeOperation='source-over';
 var vg=x.createRadialGradient(CX,CY,H*0.28,CX,H*0.5,H*0.95);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.62)');x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS = [
 ("Two Authors, One Brand", "Yarvin &amp; Land",
  "<b>Curtis Yarvin</b>, blogging as &lsquo;Mencius Moldbug&rsquo; (Unqualified Reservations, 2007-14), is the originating theorist — the Cathedral, neocameralism, the patchwork are his. <b>Nick Land</b>, the British philosopher of accelerationism, wrote the 2012 essay &lsquo;The Dark Enlightenment&rsquo; that named and popularized the umbrella. &lsquo;Neoreaction&rsquo; (NRx) and &lsquo;the Dark Enlightenment&rsquo; label the same loose cluster."),
 ("The Core Claim", "the Enlightenment as the error",
  "The unifying premise: the Enlightenment was a wrong turn and democracy / egalitarianism are failure modes. From it follow the proposals — dissolve democratic government, run the state as a corporation, and let people change rulers by leaving rather than voting."),
 ("Not the Illuminati", "the load-bearing distinction",
  "This is a REAL ideology with named authors and primary texts — <b>not</b> the antisemitic &lsquo;Illuminati / Rothschild / NWO&rsquo; conspiracy it gets conflated with. Yarvin explicitly calls the &lsquo;Cathedral&rsquo; <i>emergent and non-conspiratorial</i> — no secret cabal. (Critics argue it functions like a conspiracy theory anyway; the page keeps both.)"),
]
ARC = [
 ("The Cathedral", "Yarvin's central concept",
  "Yarvin's term for the distributed, <i>non-conspiratorial</i> complex of academia + media (+ bureaucracy) that propagates a progressive consensus with quasi-religious authority — by emergent coordination, he says, not by command. Critics call it a &lsquo;panchreston&rsquo;: an idea so all-encompassing it explains everything and therefore nothing."),
 ("Gov-Corp &amp; the Patchwork", "neocameralism",
  "Neocameralism reimagines the state as a joint-stock company: a CEO (functionally a monarch) accountable to shareholders, not voters. &lsquo;Patchwork&rsquo; multiplies that into many small competing sovereign &lsquo;patches&rsquo; — a market of governments. And &lsquo;RAGE&rsquo; (Retire All Government Employees): purge the civil service to &lsquo;reboot&rsquo; the state."),
 ("Exit, Not Voice", "the anti-democratic mechanism",
  "Borrowing Albert Hirschman's 1970 pair (exit / voice) and loading it entirely toward exit: democratic &lsquo;voice&rsquo; is devalued; the only legitimate check is leaving for another gov-corp. Land's slogan: &lsquo;No Voice, Free Exit.&rsquo; Land's broader accelerationism treats techno-capitalism as an autonomous force and democracy as a &lsquo;decelerator.&rsquo;"),
]
IDEAS = [
 ("Real Ideology vs Conspiracy Theory", "why this is in Tin-Foil but tagged REAL", [
   "It belongs in a &lsquo;line of veracity&rsquo; domain because it is fringe and extreme — but the verdict is REAL: documented authors, primary texts, a traceable genealogy.",
   "It is structurally different from the Illuminati/NWO myth: the latter posits a hidden directing cabal; the Cathedral is claimed (by its author) to be emergent. Don't conflate the two." ]),
 ("Documented vs Reported Influence", "handle with care", [
   "Documented: Peter Thiel's 2009 Cato essay (&lsquo;I no longer believe that freedom and democracy are compatible&rsquo; — his own libertarian line, not an NRx text); JD Vance citing Yarvin and &lsquo;RAGE&rsquo; in 2022; Yarvin's risen 2022-25 media profile.",
   "Reported / inferential: the strength of a Thiel-Yarvin tie, and any claim that NRx &lsquo;directs&rsquo; policy. &lsquo;Shares a milieu&rsquo; is documented; &lsquo;runs the government&rsquo; is not." ]),
 ("The Critique", "represented as critique", [
   "Most scholars/journalists call it authoritarian, antidemocratic, and the alt-right's &lsquo;theoretical branch.&rsquo;",
   "&lsquo;Neofascism&rsquo; is a label applied by named critics (Benjamin Noys; Dimitrakaki &amp; Weeks; Corey Pein's &lsquo;Mouthbreathing Machiavellis&rsquo;) — presented as their characterization, not the page's verdict." ]),
]
SECTIONS = [
 ("The Concepts &amp; Who Named Them", "the NRx vocabulary, attributed", [
   ("The Cathedral", "Yarvin", "academia + media as emergent (he says) consensus-machine; critics: a panchreston"),
   ("Neocameralism / gov-corp", "Yarvin", "the state as a joint-stock corporation under a CEO-monarch"),
   ("The Patchwork", "Yarvin", "many small competing sovereign &lsquo;patches&rsquo; — a market of governments"),
   ("Exit over Voice", "after Hirschman 1970", "&lsquo;No Voice, Free Exit&rsquo; — democracy devalued, leaving privileged (Land)"),
   ("RAGE", "Yarvin", "&lsquo;Retire All Government Employees&rsquo; — purge the civil service to reboot the state"),
   ("Accelerationism", "Land", "techno-capitalism as autonomous force; democracy a &lsquo;decelerator&rsquo; (e/acc &amp; left-accel are distinct strands)"),
 ]),
 ("The Record", "authors, influence, critique — documented vs reported", [
   ("Curtis Yarvin (Mencius Moldbug)", "Unqualified Reservations · 2007-14", "originating theorist; raised mainstream profile 2022-25"),
   ("Nick Land", "&lsquo;The Dark Enlightenment&rsquo; · 2012", "named &amp; popularized the umbrella; the accelerationist wing"),
   ("Peter Thiel", "Cato Unbound · 2009 · documented", "&lsquo;freedom and democracy&hellip; not compatible&rsquo; — his own libertarian essay, not an NRx text"),
   ("JD Vance", "cited Yarvin / RAGE · 2022 · documented", "the citation is documented; depth of commitment is interpretive"),
   ("the neofascism charge", "Noys · Pein · Dimitrakaki &amp; Weeks", "critics' characterization, attributed — not the page's voice"),
 ]),
]
EMERGENTS = [
 ("mencius-moldbug", "Mencius Moldbug", "Curtis Yarvin · the originating theorist", "natural",
  "Curtis Yarvin, writing as 'Mencius Moldbug' on the blog Unqualified Reservations (2007-14) — the foundational NRx theorist who coined the Cathedral, neocameralism, and the patchwork; his mainstream profile rose sharply 2022-25",
  "He is the source text of the movement: the pseudonymous blogger whose long posts became the doctrine, and whose return to the public eye is why this is catalogued now rather than as a closed curio."),
 ("nick-land", "Nick Land", "the namer · the accelerationist wing", "natural",
  "the British philosopher (ex-Warwick CCRU) whose 2012 essay 'The Dark Enlightenment' named and popularized the umbrella term and tied NRx to his accelerationism",
  "He is the brand and the engine: the figure who gave the cluster its name and welded it to the idea that techno-capitalism is an autonomous force democracy only slows."),
 ("the-cathedral", "The Cathedral", "the consensus-machine · emergent, he says", "ethereal",
  "Yarvin's central term for the distributed academia-plus-media complex that propagates progressive consensus with quasi-religious authority — which he insists is emergent and NON-conspiratorial, and which critics call a panchreston (explains everything, therefore nothing)",
  "It is the idea everything else hangs on, and the one that most needs the honest caveat: its author says it is not a cabal — the very thing that separates this from the Illuminati myth — while critics say it does a conspiracy theory's work regardless."),
 ("neocameralism", "Neocameralism", "gov-corp · the CEO-monarch", "electrical",
  "Yarvin's proposal to run the state as a joint-stock corporation: a CEO who is functionally a monarch, accountable to shareholders rather than voters — 'gov-corp'",
  "It is the movement's blueprint for power: government stripped of the demos and rebuilt as a company, the sharpest expression of 'democracy was the mistake.'"),
 ("the-patchwork", "The Patchwork", "a market of governments", "electrical",
  "Yarvin's vision of the world broken into many small competing sovereign 'patches,' each a neocameralist gov-corp, competing for residents",
  "It is exit made geography: a planet of micro-states you choose between like products — the structural home of 'leave, don't vote.'"),
 ("exit-over-voice", "Exit over Voice", "&lsquo;No Voice, Free Exit&rsquo;", "ethereal",
  "the recasting of economist Albert Hirschman's 1970 exit/voice pair entirely toward exit — democratic participation ('voice') devalued, leaving for another gov-corp ('exit') the only legitimate check; Land's slogan 'No Voice, Free Exit'",
  "It is the anti-democratic move in one phrase: not reform from within but flight to elsewhere — a borrowed neutral framework bent into a rejection of the vote."),
 ("rage", "RAGE", "Retire All Government Employees", "electrical",
  "Yarvin's mnemonic for purging the entire civil service to enable a 'reboot' or 'reset' of the state — cited approvingly by JD Vance in 2022",
  "It is the doctrine's operational edge: the part that stopped being theory when a sitting politician repeated it — the move from 'democracy is bad' to 'fire everyone Monday.'"),
 ("the-anti-enlightenment", "The Anti-Enlightenment", "the core thesis", "spiritual",
  "the unifying premise that the Enlightenment itself was a wrong turn and that democracy and egalitarianism are failure modes to be undone",
  "It is the root the whole tree grows from: not a policy but a verdict on three centuries — the claim that the modern settlement was an error, which makes every proposal a kind of undoing."),
 ("accelerationism", "Accelerationism", "Land's engine · contested taxonomy", "electrical",
  "Land's broader project — radical intensification of techno-capitalism toward a singularity, treating capitalism as an autonomous deterritorializing force and democracy as a 'decelerator'; note that e/acc and left-accelerationism are DISTINCT, often opposed strands (don't equate accelerationism wholesale with NRx)",
  "It is the philosophy under the politics, and a genuinely tangled one: the page flags that 'accelerationism' is not one thing, and that Land's is only one branch of a contested family."),
 ("the-thiel-essay", "The Thiel Essay", "Cato, 2009 · documented sympathy", "natural",
  "Peter Thiel's 2009 Cato Unbound essay 'The Education of a Libertarian,' containing 'I no longer believe that freedom and democracy are compatible' — his own libertarian statement, routinely cited as evidence of antidemocratic sympathy in the same tech milieu (NOT itself an NRx text)",
  "It is the most-quoted primary document of the milieu — and a test of honest sourcing: real and damning in its own words, but not the same thing as the doctrine, and the page says so."),
 ("the-vance-citation", "The Vance Citation", "2022 · documented", "natural",
  "the documented instance of JD Vance favorably citing Yarvin and the 'RAGE' concept during his 2022 Senate run — the clearest link from the doctrine to electoral politics",
  "It is where the catalogue earns its keep: a verifiable citation by a major political figure — reported by multiple outlets — held apart from the looser claim that the ideology 'runs' anything."),
 ("the-neofascism-charge", "The Neofascism Charge", "the critics, attributed", "natural",
  "the characterization by named critics — Benjamin Noys ('an acceleration of capitalism to a fascist point'), Dimitrakaki & Weeks, journalist Corey Pein ('Mouthbreathing Machiavellis Dream of a Silicon Reich') — that NRx is authoritarian, alt-right-aligned, or neofascist",
  "It is the weight of reception kept honest: presented as the critics' verdict with their names attached, not laundered into the page's own voice — criticism represented as criticism."),
 ("not-the-illuminati", "Not the Illuminati", "the veracity line · the true self", "spiritual",
  "the honest distinction this sphere exists to make: the Dark Enlightenment is a REAL, documented ideology — not the antisemitic Illuminati/Rothschild/NWO conspiracy theory it is often confused with; the Cathedral is claimed to be emergent, not a hidden cabal",
  "It is the whole point of putting this in a veracity domain: to hold the line between a real (if alarming) philosophy you can cite and a false cabal-myth you cannot — the difference between 'these people wrote this' and 'a secret group runs the world.'"),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","DRK")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","DRK")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","DRK")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"DRK · The Dark Enlightenment","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":"DRK","emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"DRK · The Dark Enlightenment — neoreaction (NRx), Yarvin & Land","nature":role,"crystallization":why,"mechanism":"Crystallized from the documented NRx corpus; research-agent-verified.","witness":"a concept or figure of the neoreactionary philosophy, examined not endorsed","conductor":"ROOT0 (catalogued into UD0)","inputs":"Yarvin; Land; the Cathedral; neocameralism; exit over voice","source":"the NRx corpus, catalogued by ROOT0"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts);out.append(f'<div class="pillar"><h3>{t}</h3><p class="ps">{s}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","ethereal");col=NATURES.get(em,("#9aa6bc",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"DRK · The Dark Enlightenment","axiom":"DRK"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Examined</h2><p class="ss">the authors, the concepts, the documented influences, and the critics&rsquo; charge, as ACI <b>.agent</b>s — examined, not endorsed ({len(ps)})</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE DARK ENLIGHTENMENT (neoreaction / NRx) — the real antidemocratic political philosophy of Curtis Yarvin and Nick Land, examined critically and not endorsed. The Cathedral, neocameralism, exit-over-voice. Veracity: REAL ideology — distinct from the antisemitic Illuminati/NWO conspiracy. A Tin-Foil-domain sphere by ROOT0.">
<title>THE DARK ENLIGHTENMENT · DRK · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#07080c;--ink2:rgba(16,18,24,0.84);--pa:#e8eaf0;--pa2:#a8b0c0;--steel:#9aa6bc;--amber:#d89030;--cyan:#46c8e0;--violet:#c060f0;--red:#d0455a;
--dim:#727a8c;--faint:rgba(150,160,185,0.16);--line:rgba(150,160,185,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#07080c}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(12,14,20,.05),rgba(3,4,7,.6) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--steel);text-decoration:none}
header{padding:30px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
.verdict{display:inline-flex;align-items:center;gap:10px;margin:0 auto 18px;padding:8px 16px;border:1px solid var(--c);border-radius:40px;background:rgba(10,14,20,0.7);font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--pa2)}
.verdict b{font-family:var(--disp);font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--c)}
.verdict .vd{width:9px;height:9px;border-radius:50%;background:var(--c);box-shadow:0 0 10px var(--c)}
h1{font-family:var(--disp);font-size:clamp(28px,6vw,54px);font-weight:900;letter-spacing:.05em;color:#fff;text-shadow:0 0 22px rgba(154,166,188,.35)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--steel);margin-top:10px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--amber)}.badge .bt .mo{color:var(--cyan)}.badge .bt a{color:var(--steel);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}.pillar h3{font-family:var(--head);font-size:16px;color:var(--amber);letter-spacing:.02em;font-weight:600}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--steel);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--steel);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--amber);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--amber);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--steel);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--steel)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--amber);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--amber)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--steel);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/ud0/#tin-foil">◄ UD0 · the Tin-Foil domain</a></div>
  <header>
    <div class="verdict" style="--c:__VCOL__"><span class="vd"></span>VERACITY · <b>__VERDICT__</b> — __VSUB__</div>
    <h1>THE DARK ENLIGHTENMENT</h1>
    <div class="tag">neoreaction · examined, not endorsed · UD0 · Tin-Foil</div>
    <p class="lede">The real antidemocratic political philosophy of <b>Curtis Yarvin</b> (&lsquo;Mencius Moldbug&rsquo;) and <b>Nick Land</b> — the Cathedral, the gov-corp run by a CEO-monarch, the patchwork of competing micro-states, and &lsquo;exit over voice.&rsquo; A documented ideology with named authors and primary texts, presented critically and not endorsed — and, crucially, <b>not</b> the antisemitic &lsquo;Illuminati / Rothschild / NWO&rsquo; conspiracy it gets confused with: Yarvin himself calls the Cathedral emergent, not a cabal. (Critics dispute that the line holds; the page keeps both.)</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE DARK ENLIGHTENMENT"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE DARK ENLIGHTENMENT</b> — neoreaction · DRK</div><div class="mo">__MONIKER__</div>
        <div>carbon · <a href="dark-enlightenment.dlw/dark-enlightenment.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="dark-enlightenment.dlw/dark-enlightenment.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the people, the concepts, the machinery, and the core claim</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Genesis</h2><p class="ss">two authors, one anti-democratic claim, and the line that isn&rsquo;t the Illuminati</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Doctrine</h2><p class="ss">the Cathedral, gov-corp &amp; the patchwork, exit-not-voice</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">real ideology vs conspiracy theory · documented vs reported · the critique</p><div class="pillars">__IDEAS__</div></section>
  __PERSONAS__
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the concepts attributed, and the documented-vs-reported influences</p></section>
  __SECTIONS__
  <div class="note"><b>Veracity verdict: REAL — examined, not endorsed.</b> The Dark Enlightenment is a genuine, documented body of political philosophy (Yarvin's Unqualified Reservations 2007-14; Land's 2012 essay), rendered here neutrally with the heavy weight of scholarly/journalistic criticism represented <b>as criticism</b> and every critique attributed to a named critic. Handle-with-care flags kept on the page: the accelerationism&harr;NRx mapping is contested (e/acc and left-accel are distinct); the Thiel&ndash;Yarvin tie is reported, not fully documented; &lsquo;cites / shares a milieu&rsquo; (documented) is held apart from &lsquo;directs policy&rsquo; (journalistic inference). The single load-bearing distinction: this is <b>NOT</b> the antisemitic Illuminati/Rothschild/NWO conspiracy — that one is false and is debunked in its own Tin-Foil sphere. Each emergent is named by its nature.</div>
  <footer>THE DARK ENLIGHTENMENT · DRK · catalogued into UD0 · the Tin-Foil domain · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/#tin-foil">← the Tin-Foil domain</a> · the .dlw badge: <a href="dark-enlightenment.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "dark-enlightenment.dlw"), "dark-enlightenment")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D).replace("__VERDICT__",VERDICT[0]).replace("__VCOL__",VERDICT[1]).replace("__VSUB__",VERDICT[2]).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ARC__",cards_html(ARC)).replace("__IDEAS__",ideas_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote THE DARK ENLIGHTENMENT (DRK) — {len(personas)} examined · badge {tok['moniker']}")
