# 2020 Jimmy Wang (JCarlson) Works
# Run this by manim.
# A peek to cryptography history, Manim source

from manimlib.imports import *

class C0S01(Scene): # Title
	def construct(self):
		title = TextMobject("A ", "Peek ","to ","Cryptography ", "History")
		subtitle = TextMobject("Jimmy Wang")
		subtitle2 = TextMobject("MATH 181 Presentation")
		
		sub1vec = np.array([0,-1.2,0])
		sub2vec = np.array([0,-2,0])
		
		subtitle.move_to(sub1vec)
		subtitle2.move_to(sub2vec)
		
		self.play(Write(title))
		self.wait(2)
		self.play(FadeInFromDown(subtitle),FadeInFromDown(subtitle2))
		#self.play()
		self.wait(3)
		
class C0S02(Scene): # Zoom in Crypt
	def construct(self):
		title = TextMobject("A ", "Peek ","to ","Cryptography ", "History")
		subtitle = TextMobject("Jimmy Wang")
		subtitle2 = TextMobject("MATH 181 Presentation")
		sub1vec = np.array([0,-1.2,0])
		sub2vec = np.array([0,-2,0])
		subtitle.move_to(sub1vec)
		subtitle2.move_to(sub2vec)
		self.add(title)
		self.add(subtitle)
		self.add(subtitle2)
		self.wait(2)
		self.play(FadeOut(title[0:3]),FadeOut(title[4]), FadeOut(subtitle), FadeOut(subtitle2))
		self.play(title[3].move_to,[0,0,0], title[3].scale, 3)
		self.wait(2)
		
class C0S03(Scene): # Add why?
	def construct(self):
		title = TextMobject("Cryptography")
		text1 = TextMobject("What is")
		text2 = TextMobject("Why")
		title.scale(3)
		text1.scale(2)
		text2.scale(2)
		self.add(title)
		self.wait(2)
		self.play(title.move_to,[0,-1,0])
		text1.move_to([0,1,0])
		text2.move_to([0,1,0])
		self.play(Write(text1))
		self.wait(5)
		self.play(Transform(text1, text2))
		self.wait(2)
		
class C0S04(Scene): # Fade Out, Trans to text1
	def construct(self):
		title = TextMobject("Cryptography")
		text2 = TextMobject("Why")
		text1 = TextMobject("The purpose of Cryptography")
		title.scale(3)
		text2.scale(2)
		text1.scale(2)
		title.move_to([0,-1,0])
		text2.move_to([0,1,0])
		self.add(title)
		self.add(text2)
		self.wait(2)
		self.play(FadeOut(title), FadeOut(text2))
		self.play(Write(text1))
		self.wait(2)
		
class C1S01(Scene): # Information
	def construct(self):
		title = TextMobject("Information").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		self.wait(5)
		infolist = TextMobject("Texts", "Voices", "Images", 
					"Animations", "Gestures", "...", alignment = "")
		
		infolist[0].move_to([-3,2,0])
		for i in np.arange(0,5):
			self.play(Write(infolist[i]), run_time = 0.5)
			self.wait(0.5)
			infolist[i+1].move_to(infolist[i].get_center() - [0, 0.8, 0])
				
		self.play(Write(infolist[5]), run_time = 1)
		self.wait(5)
		
		texts = TextMobject("Source", "Destination")
		texto = TexMobject("\\to")
		texTR = TextMobject("transmit")
		
		texto.scale(2)
		texTR.scale(0.6)
		texts[0].move_to([2,0,0])
		texts[1].move_to([5,0,0])
		texto.move_to([3.25,0,0])
		texTR.move_to(texto.get_center() - [0, 1, 0])
		
		self.play(Write(texts))
		self.wait(1)
		
		self.play(Write(texto), Write(texTR))
		self.wait(2)
			
		
class C1S02(Scene):
	def construct(self):
		title = TextMobject("Information").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		infolist = TextMobject("Texts", "Voices", "Images", 
					"Animations", "Gestures", "...", alignment = "")
		
		infolist[0].move_to([-3,2,0])
		for i in np.arange(0,5):
			infolist[i+1].move_to(infolist[i].get_center() - [0, 0.8, 0])
		self.add(infolist)
		
		texts = TextMobject("Source", "Destination")
		texto = TexMobject("\\to")
		texTR = TextMobject("transmit")
		
		texto.scale(2)
		texTR.scale(0.6)
		texts[0].move_to([2,0,0])
		texts[1].move_to([5,0,0])
		texto.move_to([3.25,0,0])
		texTR.move_to(texto.get_center() - [0, 1, 0])
		self.add(texts, texto, texTR)
		
		self.wait(2)
		
		Model = TextMobject("SRC", "$\\xrightarrow{\\hspace*{2cm}}$", "DEST")
		Model.scale(2)
		self.play(FadeOut(infolist), FadeOut(texts), FadeOut(texto), FadeOut(texTR), Write(Model))
		self.wait(5)
		
		ptext = TextMobject("plain\\_text")
		ptext.move_to(Model[0].get_center() + [0, 1, 0])
		self.play(FadeIn(ptext))
		self.wait(2)
		self.play(ptext.move_to, Model[2].get_center() + [0,1,0], run_time = 2 )
		self.wait(2)
		
class C1S03(Scene): # text to somebody else
	def construct(self):
		title = TextMobject("Information").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		

		Model = TextMobject("SRC", "$\\xrightarrow{\\hspace*{2cm}}$", "DEST")
		Model.scale(2)
		self.add(Model)
		ptext = TextMobject("plain\\_text")
		ptext.move_to(Model[0].get_center() + [0, 1, 0])
		self.add(ptext)
		self.wait(3)
		
		Snooper = TextMobject("Snooper").scale(1.3).move_to([4, 2, 0])
		self.play(Write(Snooper))
		self.wait(3)
		
		self.play(ptext.copy().move_to, Model[2].get_center() + [0,0.7,0],
				  ptext.move_to, Snooper.get_center() + [0, 0.7, 0], run_time = 2
				  )
				  
		self.wait(3)
		
class C1S04(Scene):
	def construct(self):
		title = TextMobject("Information").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		Sec = TextMobject("How to keep information \\emph{secure}?");
		Sec.scale(1.5)
		self.play(Write(Sec));
		self.wait(5)
		
		self.play(Sec.move_to, [0, 1, 0])
		self.wait(2)
		
		Model = TextMobject("PlainText", "$\\xrightarrow{\\hspace*{2cm}}$", "SecureText")
		Model.move_to([0,-1,0])
		
		Model2 = TextMobject("SecureText", "$\\xrightarrow{\\hspace*{2cm}}$", "PlainText")
		Model2.move_to([0,-2,0])
		
		self.play(Write(Model))
		
		self.wait(3)
		
		self.play(Transform(Model.copy(), Model2))
		self.wait(3)
		
class C1S05(Scene):
	def construct(self):
		title = TextMobject("Information").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		Model = TextMobject("SRC", "$\\xrightarrow{\\hspace*{2cm}}$", "DEST")
		Model.scale(2)
		self.add(Model)
		ptext = TextMobject("plain\\_text")
		ptext.move_to(Model[0].get_center() + [0, 1, 0])
		self.add(ptext)
		
		Snooper = TextMobject("Snooper").scale(1.3).move_to([4, 2, 0])
		self.add(Snooper)
		
		self.wait(3)
		
		ptext2 = TextMobject("SecureText")
		ptext2.move_to(ptext.get_center())
		
		self.play(Transform(ptext, ptext2))
		
		self.wait(3)
		
		self.play(ptext.move_to, Model[2].get_center() + [0,0.7,0],
				  ptext.copy().move_to, Snooper.get_center() + [0, 0.7, 0], run_time = 2
				  )
				  
		self.wait(3)
		
		self.play(Transform(ptext, TextMobject("plain\\_text").move_to(ptext.get_center())))
		
		self.wait(3)
		
class C1S06(Scene):
	def construct(self):
		title = TextMobject("Summary").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		summaries = TextMobject("1) Information Is Everywhere\\\\",
								"2) Info Transmittion happens between \\\\ a \\emph{source} and a \\emph{destination}\\\\",
								"3) Cryptography transforms \\emph{plaintext} \\\\ to some \\emph{secure text}, that only \\\\ \\emph{designated} receivers can transform it back",
								alignment = "");
								
		self.wait(2)
		for i in np.arange(0, 3):
			self.play(Write(summaries[i]))
			self.wait(3)
			
class C1S07(Scene):
	def construct(self):
		title = TextMobject("Summary").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		summaries = TextMobject("1) Information Is Everywhere\\\\",
								"2) Info Transmittion happens between \\\\ a \\emph{source} and a \\emph{destination}\\\\",
								"3) Cryptography transforms \\emph{plaintext} \\\\ to some \\emph{secure text}, that only \\\\ \\emph{designated} receivers can transform it back",
								alignment = "");
		self.add(summaries)
		
		next_title = TextMobject("Caesar Cipher").scale(2)
		
		self.play(FadeOut(title, run_time = 1), FadeOut(summaries, run_time = 1), Write(next_title, run_time = 2));
		
		self.wait(2)
			
class C2S01(Scene):
		
	def construct(self):
		next_title = TextMobject("Caesar Cipher").scale(2)
		title = TextMobject("Caesar Cipher").move_to([-5,3,0])
		title.scale(1.3)
		self.play(next_title.scale, 0.65, next_title.move_to, [-5,3,0])
		
		self.wait(3)
		
		caesar = ImageMobject("JuliasCaesar.jpg").scale(2)
		caption = TextMobject("Gaius Julius Caesar (100 BC - 44 BC)").next_to(caesar, DOWN, buff=1)
		self.play(FadeIn(caesar), Write(caption))
		
		self.wait(5)
		
		self.play(FadeOut(caesar), FadeOut(caption))
		
		self.wait(1)
		
class C2S02(Scene):
	def nextchar(self, ch):
		if ((ord(ch) >= 65) & (ord(ch) <= 90)):
			ls = ord(ch) - 65
			ls = (ls + 3) % 26
			return chr(ls + 65);
		return ch;
	
	def construct(self):
		title = TextMobject("Caesar Cipher").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		t0 = TextMobject("Shift by 3").scale(2)
		
		t1 = TextMobject("A $\\to$ D").scale(2)
		t2 = TextMobject("B $\\to$ E").scale(2)
		t3 = TextMobject("C $\\to$ F").scale(2)
		t4 = TexMobject("\\dots").scale(2)
		t5 = TextMobject("W $\\to$ Z").scale(2)
		t6 = TextMobject("X $\\to$ A").scale(2)
		t7 = TextMobject("Y $\\to$ B").scale(2)
		t8 = TextMobject("Z $\\to$ C").scale(2)
		
		self.play(Write(t0))
		self.wait(3)
		
		self.play(ReplacementTransform(t0, t1))
		self.wait(2)
		
		self.play(Transform(t1, t2))
		self.wait(2)
		self.play(Transform(t1, t3))
		self.wait(2)
		self.play(Transform(t1, t4))
		self.wait(3)
		
		self.play(Transform(t1, t5))
		self.wait(5)
		self.play(Transform(t1, t6))
		self.wait(3)
		self.play(Transform(t1, t7))
		self.wait(2)
		self.play(Transform(t1, t8))
		self.wait(2)
		self.play(FadeOut(t1))
		self.wait(2)
		
		

		
class C2S03(Scene):
	def nextchar(self, ch):
		if ((ord(ch) >= 65) & (ord(ch) <= 90)):
			ls = ord(ch) - 65
			ls = (ls + 3) % 26
			return chr(ls + 65);
		return ch;
	
	def construct(self):
		title = TextMobject("Caesar Cipher").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		plain = 'HISTORY OF MATHEMATICS'
		pltext = Text(plain, font='Courier New').move_to([0, 1, 0])
		
		self.play(Write(pltext))
		
		self.wait(3)
		
		new_pl = plain;
		plt = pltext.copy();
		self.play(plt.move_to, [0, -1, 0]);
		
		self.wait(3)
		
		for i in np.arange(0, 7):
			new_pl = new_pl[:i] + self.nextchar(new_pl[i]) + new_pl[i+1:];
			new_t = Text(new_pl, font='Courier New').move_to(plt);
			self.play(Transform(plt, new_t))
			self.wait(2)
		
		for i in np.arange(7, len(plain)):
			new_pl = new_pl[:i] + self.nextchar(new_pl[i]) + new_pl[i+1:];
			
		new_t = Text(new_pl, font='Courier New').move_to(plt);
		self.play(Transform(plt, new_t))
		self.wait(3)
		
			
class C3S01(Scene):
	def construct(self):
		prev_title = TextMobject("Caesar Cipher").move_to([-5,3,0])
		prev_title.scale(1.3)
		self.add(prev_title)
		self.wait(1)
		title = TextMobject("Substitution").move_to([-5,3,0])
		title.scale(1.3)
		self.play(ReplacementTransform(prev_title, title))
		
		cap1 = TextMobject(r"Generalized-Caesar\\",
						   r"Scramble the alphabet",
						   alignment = "").move_to([0,1,0])
						   
		cap2 = Text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", font = "Courier New").scale(0.8).move_to([0,-1,0])
		cap3 = Text("MBPULEOGVTIKXQNWSCFJDZRHAY", font = "Courier New").move_to([0,-2,0]).scale(0.8)
		
		self.play(Write(cap1[0]))
		self.wait(2)
		self.play(Write(cap1[1]))
		self.wait(3)
		
		self.play(Write(cap2), Write(cap2.copy()))
		self.wait(1)
		self.play(cap2.move_to, [0,-2,0])
		self.wait(1)
		self.play(Transform(cap2, cap3), run_time = 3)
		self.wait(3)


class C3S02(Scene):
	def construct(self):
		title = TextMobject("Substitution").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		cap1 = TextMobject(r"Generalized-Caesar\\",
						   r"Scramble the alphabet",
						   alignment = "").move_to([0,1,0])
		self.add(cap1)
		cap2 = Text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", font = "Courier New").scale(0.8).move_to([0,-1,0])
		cap3 = Text("MBPULEOGVTIKXQNWSCFJDZRHAY", font = "Courier New").move_to([0,-2,0]).scale(0.8)
		
		self.add(cap2,cap3)
		
		self.play(FadeOut(cap1),
				  cap2.shift, UP*2, cap3.shift, UP*2)
		
		self.wait(3)
				  
		cap4 = TexMobject("26!", r"\approx 4.03 \times 10^{26}").move_to([0,-1,0])
		cap5 = TextMobject(r"1 combination/second $\Rightarrow$ approx. $1.28 \times 10^{19}$ years").move_to([0,-2,0])
		
		self.play(Write(cap4[0]))
		self.wait(2)
		self.play(Write(cap4[1]))
		self.wait(3)
		self.play(Write(cap5))
		self.wait(3)


class C3S03(Scene):
	def construct(self):
		title = TextMobject("Substitution").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		self.wait(2)
		
		freqimg = ImageMobject("ELF_BCK.png").scale(2.6)
		cap1 = TextMobject("Frequency Analysis").next_to(freqimg, DOWN, buff = 0.4)
		
		self.play(FadeIn(freqimg),
				  Write(cap1));
		
		self.wait(2)
		
class C4S01(Scene):
	def construct(self):
		prev_title = TextMobject("Substitution").move_to([-5,3,0])
		prev_title.scale(1.3)
		self.add(prev_title)
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		
		freqimg = ImageMobject("ELF_BCK.png").scale(2.6)
		cap1 = TextMobject("Frequency Analysis").next_to(freqimg, DOWN, buff = 0.4)
		self.add(freqimg, cap1)
		
		self.wait(2)
		self.play(ReplacementTransform(prev_title, title), FadeOut(freqimg), FadeOut(cap1))
		
		quote = """
MTS SR JUR RMWJWRA OM J WURJI YOVOD SJU IRGIOMW SHRIHRU
IHJI MJIOTM TU JML MJIOTM GT YTMYROVRA JMA GT ARAOYJIRA
YJM DTMW RMAPUR SR JUR QRI TM J WURJI CJIIDRNORDA TN IHJI
SJU SR HJVR YTQR IT ARAOYJIR J FTUIOTM TN IHJI NORDA
JG J NOMJD URGIOMW FDJYR NTU IHTGR SHT HRUR WJVR IHROU
DOVRG IHJI IHJI MJIOTM QOWHI DOVR OI OG JDITWRIHRU NOIIOMW
JMA FUTFRU IHJI SR GHTPDA AT IHOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)
		
		self.play(FadeIn(txt))
			
		self.wait(3)
	
class C4S02(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
MTS SR JUR RMWJWRA OM J WURJI YOVOD SJU IRGIOMW SHRIHRU
IHJI MJIOTM TU JML MJIOTM GT YTMYROVRA JMA GT ARAOYJIRA
YJM DTMW RMAPUR SR JUR QRI TM J WURJI CJIIDRNORDA TN IHJI
SJU SR HJVR YTQR IT ARAOYJIR J FTUIOTM TN IHJI NORDA
JG J NOMJD URGIOMW FDJYR NTU IHTGR SHT HRUR WJVR IHROU
DOVRG IHJI IHJI MJIOTM QOWHI DOVR OI OG JDITWRIHRU NOIIOMW
JMA FUTFRU IHJI SR GHTPDA AT IHOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)
		
		self.add(txt)
			
		self.wait(3)
		
		FreqRepl = TextMobject("Count individual symbols appearence").next_to(txt, DOWN, buff = 0.5)
		
		self.play(Write(FreqRepl))
		
		self.wait(5)
		
		Freq2 = TextMobject("R appears most, 39 times $\\to$ e").move_to(FreqRepl.get_center())
		
		self.play(Transform(FreqRepl, Freq2))
		
		self.wait(3)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'R': '#FF0000'}).scale(0.35)
		
		self.play(FadeOut(txt), FadeIn(colortxt))
		
		self.wait(2)
		
		newquote = quote.replace("R", "e");
		newtxt = Text(newquote, font = "Courier New", stroke_width = 0).scale(0.35)
		
		self.play(FadeOut(colortxt), FadeIn(newtxt))
		
		self.wait(2)
		
		Freq3 = TextMobject("next is I, 37 times $\\to$ t").move_to(FreqRepl.get_center())
		
		self.play(Transform(FreqRepl, Freq3))
		
		self.wait(2)
		
		color2txt = Text(newquote, font="Courier New",stroke_width = 0,
						t2c={'I': '#FF0000'}).scale(0.35)
						
		self.play(FadeOut(newtxt), FadeIn(color2txt))
		self.wait(1)
		
		new2quote = newquote.replace("I", "t");
		new2txt = Text(new2quote, font = "Courier New", stroke_width = 0).scale(0.35)
		
		self.play(FadeOut(color2txt), FadeIn(new2txt), FadeOut(FreqRepl))
		
		self.wait(2)
					
class C4S03(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
MTS Se JUe eMWJWeA OM J WUeJt YOVOD SJU teGtOMW SHetHeU
tHJt MJtOTM TU JML MJtOTM GT YTMYeOVeA JMA GT AeAOYJteA
YJM DTMW eMAPUe Se JUe Qet TM J WUeJt CJttDeNOeDA TN tHJt
SJU Se HJVe YTQe tT AeAOYJte J FTUtOTM TN tHJt NOeDA
JG J NOMJD UeGtOMW FDJYe NTU tHTGe SHT HeUe WJVe tHeOU
DOVeG tHJt tHJt MJtOTM QOWHt DOVe Ot OG JDtTWetHeU NOttOMW
JMA FUTFeU tHJt Se GHTPDA AT tHOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("Notice the word ``tHJt\"",
					tex_to_color_map={"tHJt": '#FF0000'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'tHJt': '#FF0000'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'tHJt': '#FF0000', 'H': '#FF0000', 'J': '#FF0000'}).scale(0.35)
		Caption2 = TextMobject("Replace H with h, J with a").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("H", "h").replace("J", "a")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
class C4S04(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
MTS Se aUe eMWaWeA OM a WUeat YOVOD SaU teGtOMW ShetheU
that MatOTM TU aML MatOTM GT YTMYeOVeA aMA GT AeAOYateA
YaM DTMW eMAPUe Se aUe Qet TM a WUeat CattDeNOeDA TN that
SaU Se haVe YTQe tT AeAOYate a FTUtOTM TN that NOeDA
aG a NOMaD UeGtOMW FDaYe NTU thTGe ShT heUe WaVe theOU
DOVeG that that MatOTM QOWht DOVe Ot OG aDtTWetheU NOttOMW
aMA FUTFeU that Se GhTPDA AT thOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("two-letter word ``tT\" $\\to$ to",
					tex_to_color_map={"tT": '#FF0000'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' tT ': '#FF0000'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'tT': '#FF0000', 'T': '#FF0000'}).scale(0.35)
		Caption2 = TextMobject("Replace T with o").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("T", "o")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)

class C4S05(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
MoS Se aUe eMWaWeA OM a WUeat YOVOD SaU teGtOMW ShetheU
that MatOoM oU aML MatOoM Go YoMYeOVeA aMA Go AeAOYateA
YaM DoMW eMAPUe Se aUe Qet oM a WUeat CattDeNOeDA oN that
SaU Se haVe YoQe to AeAOYate a FoUtOoM oN that NOeDA
aG a NOMaD UeGtOMW FDaYe NoU thoGe Sho heUe WaVe theOU
DOVeG that that MatOoM QOWht DOVe Ot OG aDtoWetheU NOttOMW
aMA FUoFeU that Se GhoPDA Ao thOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``haVe\" $\\to$ have, ``ShetheU\" $\\to$ whether",
					tex_to_color_map={"haVe": '#FF0000', 'ShetheU': '#0000FF'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' haVe ': '#FF0000', 'ShetheU': '#0000FF'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' haVe ': '#FF0000', 'ShetheU': '#0000FF',
							'V':'#FF0000', 'S': '#0000FF', 'U': '#0000FF'}).scale(0.35)
		Caption2 = TextMobject("Replace V with v, S with w, U with r").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("V", "v").replace("S", 'w').replace('U', 'r')
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)

class C4S06(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
Mow we are eMWaWeA OM a Wreat YOvOD war teGtOMW whether
that MatOoM or aML MatOoM Go YoMYeOveA aMA Go AeAOYateA
YaM DoMW eMAPre we are Qet oM a Wreat CattDeNOeDA oN that
war we have YoQe to AeAOYate a FortOoM oN that NOeDA
aG a NOMaD reGtOMW FDaYe Nor thoGe who here Wave theOr
DOveG that that MatOoM QOWht DOve Ot OG aDtoWether NOttOMW
aMA FroFer that we GhoPDA Ao thOG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``Ot\" , ``theOr\"",
					tex_to_color_map={"Ot": '#FF0000', 'theOr': '#FF0000'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' Ot ': '#FF0000', 'theOr': '#FF0000'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' Ot ': '#FF0000', 'theOr': '#FF0000',
							'O':'#FF0000'}).scale(0.35)
		Caption2 = TextMobject("Replace O with i").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("O", "i")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)

class C4S07(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
Mow we are eMWaWeA iM a Wreat YiviD war teGtiMW whether
that MatioM or aML MatioM Go YoMYeiveA aMA Go AeAiYateA
YaM DoMW eMAPre we are Qet oM a Wreat CattDeNieDA oN that
war we have YoQe to AeAiYate a FortioM oN that NieDA
aG a NiMaD reGtiMW FDaYe Nor thoGe who here Wave their
DiveG that that MatioM QiWht Dive it iG aDtoWether NittiMW
aMA FroFer that we GhoPDA Ao thiG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``MatioM'' $\\to$ nation",
					tex_to_color_map={"MatioM": '#FF0000'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' MatioM ': '#FF0000'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={' MatioM ': '#FF0000',
							'M':'#FF0000'}).scale(0.35)
		Caption2 = TextMobject("Replace M with n").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("M", "n")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
class C4S08(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
now we are enWaWeA in a Wreat YiviD war teGtinW whether
that nation or anL nation Go YonYeiveA anA Go AeAiYateA
Yan DonW enAPre we are Qet on a Wreat CattDeNieDA oN that
war we have YoQe to AeAiYate a Fortion oN that NieDA
aG a NinaD reGtinW FDaYe Nor thoGe who here Wave their
DiveG that that nation QiWht Dive it iG aDtoWether NittinW
anA FroFer that we GhoPDA Ao thiG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``FroFer'' $\\to$ proper, ``aDtoWether'' $\\to$ altogether",
					tex_to_color_map={"FroFer": '#FF0000', 'aDtoWether': '#0000FF'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'FroFer': '#FF0000', 'aDtoWether': '#0000FF'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={'FroFer': '#FF0000', 'aDtoWether': '#0000FF',
							'F':'#FF0000', 'D':'#0000FF', 'W': '#0000FF'}).scale(0.35)
		Caption2 = TextMobject("Replace F with p, D with l, W with g").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("F", "p").replace("D", "l").replace("W", "g")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
class C4S09(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
now we are engageA in a great Yivil war teGting whether
that nation or anL nation Go YonYeiveA anA Go AeAiYateA
Yan long enAPre we are Qet on a great CattleNielA oN that
war we have YoQe to AeAiYate a portion oN that NielA
aG a Ninal reGting plaYe Nor thoGe who here gave their
liveG that that nation Qight live it iG altogether Nitting
anA proper that we GhoPlA Ao thiG"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``engageA'' $\\to$ engaged, ``Yivil war'' $\\to$ civil war, ``thiG'' $\\to$ this",
					tex_to_color_map={"engageA": '#FF0000', 'Yivil': '#0000FF', 'thiG': '#00FF00'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={"engageA": '#FF0000', 'Yivil': '#0000FF', 'thiG': '#00FF00'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={"engageA": '#FF0000', 'Yivil': '#0000FF', 'thiG': '#00FF00',
							'A':'#FF0000', 'Y':'#0000FF', 'G': '#00FF00'}).scale(0.35)
		Caption2 = TextMobject("Replace A with d, Y with c, G with s").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("A", "d").replace("Y", "c").replace("G", "s")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
class C4S10(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
now we are engaged in a great civil war testing whether
that nation or anL nation so conceived and so dedicated
can long endPre we are Qet on a great CattleNield oN that
war we have coQe to dedicate a portion oN that Nield
as a Ninal resting place Nor those who here gave their
lives that that nation Qight live it is altogether Nitting
and proper that we shoPld do this"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``CattleNield'' $\\to$ battlefield, ``shoPld'' $\\to$ should",
					tex_to_color_map={"CattleNield": '#FF0000', 'shoPld': '#0000FF'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={"CattleNield": '#FF0000', 'shoPld': '#0000FF'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		colortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={"CattleNield": '#FF0000', 'shoPld': '#0000FF',
							'C':'#FF0000', 'P':'#0000FF', 'N': '#FF0000'}).scale(0.35)
		Caption2 = TextMobject("Replace C with b, N with f, P with u").move_to(Caption.get_center())
		self.play(FadeOut(precolortxt), FadeIn(colortxt), Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("C", "b").replace("N", "f").replace("P", "u")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(colortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
class C4S11(Scene):
	def construct(self):
		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
now we are engaged in a great civil war testing whether
that nation or anL nation so conceived and so dedicated
can long endure we are Qet on a great battlefield of that
war we have coQe to dedicate a portion of that field
as a final resting place for those who here gave their
lives that that nation Qight live it is altogether fitting
and proper that we should do this"""
			
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)		
		self.add(txt)
		self.wait(2)
		Caption = TextMobject("``anL'' $\\to$ any, ``coQe'', ``Qet'', ``Qight''",
					tex_to_color_map={"anL": '#FF0000', 'Q': '#0000FF'}).next_to(txt, DOWN, buff = 0.5)
		precolortxt = Text(quote, font="Courier New",stroke_width = 0,
						t2c={"anL": '#FF0000', 'Q': '#0000FF'}).scale(0.35)
		self.play(Write(Caption), FadeOut(txt), FadeIn(precolortxt))
		self.wait(5)
		
		Caption2 = TextMobject("Replace L with y, Q with m").move_to(Caption.get_center())
		self.play(Transform(Caption, Caption2))
		self.wait(3)
		
		newquote = quote.replace("L", "y").replace("Q", "m")
		newtxt = Text(newquote, font="Courier New",stroke_width = 0).scale(0.35)
		self.play(FadeOut(precolortxt), FadeIn(newtxt), FadeOut(Caption))
		self.wait(2)
		
		done = TextMobject("Done!").move_to(Caption.get_center())
		
		self.play(Write(done))
		self.wait(2)
		
class C5S01(Scene):
	def construct(self):

		title = TextMobject("Example").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		
		quote = """
now we are engaged in a great civil war testing whether
that nation or any nation so conceived and so dedicated
can long endure we are met on a great battlefield of that
war we have come to dedicate a portion of that field
as a final resting place for those who here gave their
lives that that nation might live it is altogether fitting
and proper that we should do this"""
		txt = Text(quote, font="Courier New",stroke_width = 0).scale(0.35)
		self.add(txt)
		Caption = TextMobject("Done!").next_to(txt, DOWN, buff = 0.5)
		self.add(Caption)
		self.wait(2)
		
		title_trans = TextMobject("Other Ciphers").move_to(title.get_center()).scale(1.3)
		self.play(Transform(title, title_trans),
				  FadeOut(txt), FadeOut(Caption))
				  
		self.wait(3)
		
		others = TextMobject("Vigen\`ere Cipher\\\\", "Telephone Keypad Cipher\\\\", "Rail Fence Cipher\\\\",
							"Dancing Men (Sherlock Holmes)\\\\", "Pigpen Cipher\\\\", "Book Code\\\\", "$\\dots$", alignment = "")
		for i in np.arange(0, 7):
			self.play(Write(others[i]))
			self.wait(1)
		
class C5S02(Scene):
	def construct(self):

		title = TextMobject("Other Ciphers").move_to([-5,3,0])
		title.scale(1.3)
		self.add(title)
		others = TextMobject("Vigen\`ere Cipher\\\\", "Telephone Keypad Cipher\\\\", "Rail Fence Cipher\\\\",
							"Dancing Men (Sherlock Holmes)\\\\", "Pigpen Cipher\\\\", "Book Code\\\\", "$\\dots$", alignment = "")
		self.add(others)

		self.wait(2)
		
		TFW = TextMobject("Thanks for watching!").scale(2)
		
		self.play(FadeOut(title), FadeOut(others), Write(TFW))
		self.play(TFW.shift, UP*2)
		
		titles = TextMobject("A ", "Peek ","to ","Cryptography ", "History")
		subtitle = TextMobject("Jimmy Wang")
		subtitle2 = TextMobject("MATH 181 Presentation")
		
		sub1vec = np.array([0,-1.2,0])
		sub2vec = np.array([0,-2,0])
		
		subtitle.move_to(sub1vec)
		subtitle2.move_to(sub2vec)
		
		self.play(Write(titles), Write(subtitle), Write(subtitle2))
		self.wait(3)