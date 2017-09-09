with open("dictionary.txt",'r') as d:
	txt = d.read().split()
while True:
	word = input("\nEnter word : ").upper()	
	print('\n')
	caps = ['[NL.,','[NL.:','(OF.', '(AS.', '(B.', '(GR.', '(J.', '(R.', '(F.', '(L.', '(X.', '(CO.', '(CH.', '(NL.', '(D.', '(III.', '(P.', '(NH.', '(S.', '(OL.', '(T.', '(Q.', '(I.', '(A.', '(V.', '(U.', '(C.', '(E.', '(LL.', '(H.', '(G.', '(K.', '(M.', '(Z.', '(OE.', '(Y.', '(N.', '(O.','I','U.S.]','A','CO.', 'GR.', 'SW.', 'CCTV.', 'XVIII.', '[IT.', 'EF.', 'OE.', '[FF.', 'N.', 'L.]', 'I.]', 'R.', 'YHVH.]', 'NL.]', '[NL.', 'III.', 'XIII.', 'DBC.', 'B.', 'AMEN.', '[OF.]', 'HCO.', 'XI.', 'F.]', '[AS.]', 'MHG.', 'XVI.', 'FL.', '[L.', '[OD.', 'S.', 'CC.', 'VI.', '[U.', 'CHO.', 'MR.', 'ON.', 'SO.', '[C.', 'MSS.', '[W.]', 'I.', 'BK.', '[P.]', 'AR.', '[O.', '[OR.', 'E.', 'OL.', 'ADV.', '[OWE.', 'IRS.', 'XIV.', 'T.', 'FR.', 'OD.', 'CS.', 'GOUR.]', '[G.', '[I.', '[ME.', '[ML.', 'V.', '[A.', 'AC.', 'Q.', 'III.]', 'DR.', 'MLG.', 'YII.', 'HO.', '[CF.', 'AX.', '[SA.', '[S.', 'PURPOSE.', 'LLL.', 'FF.', 'IY.', 'OF.', 'OLG.', 'AB.', 'LG.', '[N.', 'OHG.', 'DO.', '[D.]', 'NL.', '[D.', 'MNG.', '[OE.', '[OP.', 'A.]', '[OE.]', 'LX.', 'II.', 'CF.', 'ASS.', 'MRS.', 'NOL.', 'L.', 'E.]', '[LL.]', 'OH.', 'MM.', '[R.', '[NL.]', 'VIII.', 'PROS.', 'C.', 'W.', 'U.', 'DAMAGE.', 'V.]', 'SK.', 'CI.', 'D.]', '[LG.', '[L.]', 'O.', 'OS.', 'SOS.', 'G.]', 'VII.', '[GR.', 'IX.', '[AC.', 'XXX.', '[G.]', 'LL.', '[P.', '[W.', 'H.', 'HG.', 'MS.', 'ONG.', 'A.', 'SP.', 'IV.', '[Q.', 'SH.', 'Z.', 'F.', 'R.]', 'VIII.]', '[AAS.', 'X.', 'D.', 'M.', 'NO.', 'KSH.', 'K.', '[E.', 'C.]', 'XIV.]', 'OI.', 'J.', 'P.', '[F.', 'BOA.', '[F.]', 'S.]', 'OG.', 'XP.', 'OHS.', 'CH.', '[LL.', '[AS.', 'COOH.', 'GOTHIC.', '[FR.', '[OF.', 'OW.', 'G.', '[SP.', 'Y.', '[B.', '[R.]', 'ASH.', 'AS.', 'Y.]', 'II.]', 'X.]', 'NONCON.', 'IHVH.', 'TT.', 'NH.']
	nums = ['80.', '34.', '55.', '49.', '96.', '3.', '54.', '57.', '74.', '32.', '27.', '63.', '48.', '88.', '06.', '72.', '19.', '95.', '25.', '28.', '52.', '37.', '24.', '60.', '47.', '16.', '42.', '70.', '76.', '21.', '85.', '82.', '39.', '71.', '05.', '77.', '81.', '90.', '41.', '2.', '97.', '62.', '5.', '65.', '22.', '53.', '6.', '11.', '94.', '00.', '51.', '83.', '84.', '31.', '59.', '7.', '89.', '18.', '75.', '30.', '33.', '93.', '91.', '0.', '4.', '98.', '68.', '40.', '79.', '87.', '29.', '1.', '17.', '78.', '14.', '13.', '61.', '23.', '02.', '07.', '04.', '35.', '67.', '38.', '9.', '43.', '46.', '73.', '09.', '58.', '03.', '86.', '92.', '56.', '12.', '44.', '20.', '45.', '08.', '8.', '64.', '26.', '66.', '69.', '50.', '99.', '01.', '36.', '15.', '10.']
	for i,w in enumerate(txt):
		if w == word:
			j = 1
			if txt[i+j].isupper() and txt[i+j] not in caps:
				break
			while not txt[i+j].isupper() or txt[i+j] in caps:
				if txt[i+j] in nums:
					print("\n")
				print("".join(txt[i+j]),end = " ")
				j += 1				
	else:
		print("\n")
	