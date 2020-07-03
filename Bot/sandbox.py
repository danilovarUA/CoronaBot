import random

big = """🏠 ☀️ Pluviam 1.5 ☀️ [273] l+k://coordinates?16438,16338&230
🏠 ☀️  4 🐗 [134] l+k://coordinates?16421,16386&230
🏠 ☀️ 04 [279] l+k://coordinates?16439,16351&230
🏠 ☀️ Pluviam 2.4 ☀️ [199] l+k://coordinates?16449,16328&230
🏠 ☀️ Pluviam 2.3 ☀️ [265] l+k://coordinates?16451,16330&230
🏠 ☀️ Pluviam 1.3 ☀️ [276] l+k://coordinates?16437,16333&230
🏠 ☀️ Pluviam 2.5 ☀️ [216] l+k://coordinates?16448,16330&230
🏠 🌒 Black Knight 15⚔️ [277] l+k://coordinates?16436,16370&230
🏠 ☀️ Gamma 1.2 ☀️ [261] l+k://coordinates?16432,16363&230
🏠 ☀️ Pluviam 1.4 ☀️ [274] l+k://coordinates?16438,16337&230
🏠 🌒 Black Knight  6⚔️ [286] l+k://coordinates?16442,16386&230
🏠 ☀️ 07 [270] l+k://coordinates?16436,16361&230
🏠 🌒 Black Knight 16⚔️ [271] l+k://coordinates?16435,16371&230
🏠 ☀️ 02 [272] l+k://coordinates?16436,16358&230
🏠 ☀️ 05 [271] l+k://coordinates?16439,16354&230
🏠 ☀️  3 🐗 [174] l+k://coordinates?16419,16381&230
🏠 FB Fo 333-04 [251] l+k://coordinates?16435,16366&230
🏠 🌒 Black Knight 18⚔️ [271] l+k://coordinates?16437,16372&230
🏠 ☀️ Gamma 2.1 ☀️ [284] l+k://coordinates?16438,16371&230
🏠 ☀️ Pluviam 1.2 ☀️ [277] l+k://coordinates?16437,16335&230
🏠 ☀️ 06 [260] l+k://coordinates?16437,16358&230
🏠 ☀️ Pluviam 2.1 ☀️ [251] l+k://coordinates?16450,16332&230
🏠 ☀️ Pluviam 2.2 ☀️ [243] l+k://coordinates?16449,16334&230
🏠 🌒 Black Knight 10⚔️ [284] l+k://coordinates?16443,16387&230
🏠 ☀️ 01 [285] l+k://coordinates?16436,16357&230
🏠 🌒 Black Knight 35⚔️ [266] l+k://coordinates?16439,16343&230
🏠 🌒 Black Knight 39⚔️ [206] l+k://coordinates?16439,16339&230
🏠 ☀️ Gamma 2.5 ☀️ [208] l+k://coordinates?16438,16367&230
🏠 ☀️ Gamma 1.3 ☀️ [267] l+k://coordinates?16433,16363&230
🏠 ☀️ Gamma 2.3 ☀️ [281] l+k://coordinates?16437,16369&230
🏠 ☀️ Gamma 1.4 ☀️ [269] l+k://coordinates?16433,16362&230
🏠 ☀️  2 🐗 [256] l+k://coordinates?16422,16381&230
🏠 ☀️ Gamma 1.5 ☀️ [262] l+k://coordinates?16434,16363&230
🏠 ☀️ 03 [272] l+k://coordinates?16437,16360&230
🏠 🌒 Black Knight 14⚔️ [276] l+k://coordinates?16436,16372&230
🏠 🌒 Black Knight  9⚔️ [282] l+k://coordinates?16443,16386&230
🏠 🌒 Black Knight 38⚔️ [226] l+k://coordinates?16439,16337&230
🏠 ☀️ 🥳  1☀️ [250] l+k://coordinates?16414,16348&230
🏠 🌒 Black Knight  8⚔️ [285] l+k://coordinates?16440,16385&230
🏠 ☀️ Gamma 2.2 ☀️ [269] l+k://coordinates?16437,16373&230
🏠 🌒 Black Knight  7⚔️ [286] l+k://coordinates?16441,16386&230
🏠 ☀️ Gamma 1.6 ☀️ [193] l+k://coordinates?16434,16360&230
🏠 ☀️  1 🐗 [284] l+k://coordinates?16420,16383&230
🏠 ☀️ Gamma 2.4 ☀️ [280] l+k://coordinates?16439,16370&230
🏠 ☀️ Gamma 1.1 ☀️ [273] l+k://coordinates?16431,16363&230
🏠 Free Knight1899 [126] l+k://coordinates?16440,16379&230
🏠 ☀️ Pluviam 1.1 ☀️ [278] l+k://coordinates?16438,16336&230
🏰 ☀️ Till this Day 👊 1 ☀️ [1711] l+k://coordinates?16444,16392&230
🏠 🐗⚔️BD 05⚔️🐗 [281] l+k://coordinates?16443,16372&230
🏠 🐗⚔️Ty Gwynn 11⚔️🐗 [258] l+k://coordinates?16445,16366&230
🏠 🐗⚔️Winterfell1️⃣7️⃣⚔️🐗 [269] l+k://coordinates?16437,16382&230
🏠 Free Knight3419 [289] l+k://coordinates?16437,16381&230
🏠 🏠 004 🏡 [286] l+k://coordinates?16436,16385&230
🏠 🐗⚔️Johnstone⚔️🐗 [263] l+k://coordinates?16462,16347&230
🏠 🐗⚔️Abergawennie⚔️🐗 [263] l+k://coordinates?16466,16347&230
🏠 🐗⚔️Aberfeldy⚔️🐗 [266] l+k://coordinates?16468,16347&230
🏠 🐗⚔️ FB 04 ⚔️🐗 [267] l+k://coordinates?16472,16347&230
🏠 🐗⚔️MRay06⚔️🐗 [224] l+k://coordinates?16467,16347&230
🏠 🐗⚔️CH-15⚔️🐗 [209] l+k://coordinates?16448,16360&230
🏠 🐗⚔️CH-5⚔️🐗 [283] l+k://coordinates?16449,16357&230
🏠 🐗⚔️CH-8⚔️🐗 [271] l+k://coordinates?16451,16354&230
🏠 🐗⚔️BD 09⚔️🐗 [264] l+k://coordinates?16443,16370&230
🏠 🐗⚔️BD 04⚔️🐗 [279] l+k://coordinates?16441,16373&230
🏠 🐗⚔️BD 03⚔️🐗 [281] l+k://coordinates?16440,16375&230
🏠 🐗⚔️Winterfell0️⃣4️⃣⚔️🐗 [280] l+k://coordinates?16435,16385&230
🏠 🏠 001 🏡 [288] l+k://coordinates?16437,16389&230
🏠 🏠 002 🏡 [287] l+k://coordinates?16437,16388&230
🏠 ｬཞ ✞ ཀ Σ 🐒008 [275] l+k://coordinates?16445,16364&230
🏠 🐗⚔️Prinz Valium IV ⚔️🐗 [248] l+k://coordinates?16464,16346&230
🏠 🐗⚔️ FB 13 ⚔️🐗 [274] l+k://coordinates?16473,16346&230
🏠 🐗⚔️ FB 06 ⚔️🐗 [266] l+k://coordinates?16470,16346&230
🏠 🐗⚔️CH-4⚔️🐗 [281] l+k://coordinates?16449,16356&230
🏠 Free Knight1785 [237] l+k://coordinates?16439,16375&230
🏠 Hupe [247] l+k://coordinates?16438,16377&230
🏠 Free Knight1760 [246] l+k://coordinates?16437,16380&230
🏠 🐗⚔️BD 10⚔️🐗 [258] l+k://coordinates?16441,16371&230
🏠 🐗⚔️Ty Gwynn 10⚔️🐗 [254] l+k://coordinates?16443,16365&230
🏠 🐗⚔️Ty Gwynn 06⚔️🐗 [255] l+k://coordinates?16443,16366&230
🏠 🐗⚔️chrisi0️⃣3️⃣⚔️🐗 [272] l+k://coordinates?16435,16382&230
🏠 🐗⚔️Winterfell0️⃣2️⃣⚔️🐗 [282] l+k://coordinates?16434,16385&230
🏠 🏠 003 🏡 [287] l+k://coordinates?16435,16387&230
🏠 🏠 000 🏡 [289] l+k://coordinates?16437,16390&230
🏠 ｬཞ ✞ ཀ Σ 🐒003 [276] l+k://coordinates?16444,16364&230
🏠 🐗⚔️SKRAAA⚔️🐗 [290] l+k://coordinates?16445,16362&230
🏠 ｬཞ ✞ ཀ Σ 🐒014 [278] l+k://coordinates?16445,16361&230
🏠 🐗⚔️Ʀг††εƦ🐌Ʀø$$⚔️🐗 [289] l+k://coordinates?16446,16360&230
🏠 🐗⚔️Aberdeen⚔️🐗 [263] l+k://coordinates?16468,16345&230
🏠 🐗⚔️ FB 03 ⚔️🐗 [265] l+k://coordinates?16471,16345&230
🏠 🐗⚔️CH-11⚔️🐗 [237] l+k://coordinates?16447,16357&230
🏠 Free Knight1700 [240] l+k://coordinates?16437,16378&230
🏠 Free Knight1673 [243] l+k://coordinates?16438,16376&230
🏠 🐗⚔️Ty Gwynn 08⚔️🐗 [254] l+k://coordinates?16442,16366&230
🏠 🐗⚔️Winterfell0️⃣1️⃣⚔️🐗 [288] l+k://coordinates?16433,16385&230
🏠 🐗⚔️chrisi0️⃣1️⃣⚔️🐗 [277] l+k://coordinates?16433,16384&230
🏠 🐗⚔️Teufelsbraten0️⃣1️⃣⚔️🐗 [273] l+k://coordinates?16433,16383&230
🏠 🐗⚔️Winterfell0️⃣8️⃣⚔️🐗 [280] l+k://coordinates?16435,16388&230
🏠 Free Knight8909 [290] l+k://coordinates?16435,16379&230
🏠 🏠 013 🏡 [273] l+k://coordinates?16436,16391&230
🏠 ｬཞ ✞ ཀ Σ 🐒004 [278] l+k://coordinates?16443,16364&230
🏠 🔱✊ HE FON 0️⃣0️⃣3️⃣ [226] l+k://coordinates?16450,16350&230
🏠 🐗⚔️Prinz Valium V ⚔️🐗 [238] l+k://coordinates?16464,16344&230
🏠 🐗⚔️Ormakleith⚔️🐗 [264] l+k://coordinates?16459,16344&230
🏠 🐗⚔️ FB 02 ⚔️🐗 [271] l+k://coordinates?16470,16344&230
🏠 🐗⚔️CH-Z1⚔️🐗 [290] l+k://coordinates?16447,16355&230
🏠 🐗⚔️CH-12⚔️🐗 [232] l+k://coordinates?16449,16352&230
🏠 🐗⚔️CH-3⚔️🐗 [283] l+k://coordinates?16448,16353&230
🏠 Free Knight2535 [246] l+k://coordinates?16438,16374&230
🏠 🐗⚔️BD 13⚔️🐗 [239] l+k://coordinates?16444,16362&230
🏠 🐗⚔️Winterfell0️⃣7️⃣⚔️🐗 [278] l+k://coordinates?16434,16388&230
🏠 🐗⚔️Winterfell0️⃣6️⃣⚔️🐗 [280] l+k://coordinates?16433,16382&230
🏠 🐗⚔️Winterfell1️⃣5️⃣⚔️🐗 [273] l+k://coordinates?16433,16387&230
🏠 Free Knight1580 [289] l+k://coordinates?16435,16378&230
🏠 ｬཞ ✞ ཀ Σ 🐒006 [278] l+k://coordinates?16441,16365&230
🏠 ｬཞ ✞ ཀ Σ 🐒001 [281] l+k://coordinates?16443,16362&230
🏠 ｬཞ ✞ ཀ Σ 🐒010 [275] l+k://coordinates?16442,16364&230
🏠 🐗⚔️Glenburgie⚔️🐗 [263] l+k://coordinates?16461,16343&230
🏠 🐗⚔️CH-2⚔️🐗 [289] l+k://coordinates?16447,16353&230
🏠 🐗⚔️Ty Gwynn 09⚔️🐗 [255] l+k://coordinates?16440,16365&230
🏠 🐗⚔️Winterfell0️⃣5️⃣⚔️🐗 [285] l+k://coordinates?16432,16386&230
🏠 🐗⚔️chrisi0️⃣2️⃣⚔️🐗 [271] l+k://coordinates?16433,16380&230
🏠 🐗⚔️chrisi0️⃣4️⃣⚔️🐗 [254] l+k://coordinates?16434,16378&230
🏠 🐗⚔️Winterfell1️⃣0️⃣⚔️🐗 [281] l+k://coordinates?16433,16389&230
🏠 Free Knight1532 [288] l+k://coordinates?16436,16374&230
🏠 Free Knight1523 [288] l+k://coordinates?16435,16376&230
🏠 🐗⚔️Prinz Valium III ⚔️🐗 [253] l+k://coordinates?16464,16342&230
🏠 🐗⚔️Prinz Valium VII ⚔️🐗 [228] l+k://coordinates?16463,16342&230
🏠 🐗⚔️Invergarry⚔️🐗 [265] l+k://coordinates?16459,16342&230
🏠 🐗⚔️Balmakeith⚔️🐗 [264] l+k://coordinates?16458,16342&230
🏠 🐗⚔️Kildrummie⚔️🐗 [262] l+k://coordinates?16461,16342&230
🏠 🐗⚔️Langer 3⚔️🐗P [207] l+k://coordinates?16452,16342&230
🏠 🐗⚔️CH-13⚔️🐗 [248] l+k://coordinates?16446,16354&230
🏠 🐗⚔️Winterfell2️⃣2️⃣⚔️🐗 [269] l+k://coordinates?16443,16358&230
🏠 🐗⚔️Winterfell1️⃣1️⃣⚔️🐗 [273] l+k://coordinates?16431,16386&230
🏠 🐗⚔️Winterfell1️⃣8️⃣⚔️🐗 [266] l+k://coordinates?16431,16381&230
🏠 🐗⚔️Winterfell2️⃣3️⃣⚔️🐗 [268] l+k://coordinates?16444,16356&230
🏠 ｬཞ ✞ ཀ Σ 🐒012 [277] l+k://coordinates?16438,16368&230
🏠 SHOCKWAVE [276] l+k://coordinates?16431,16382&230
🏠 🐗⚔️ Die Ruine 01 ⚔️🐗 [213] l+k://coordinates?16449,16345&230
🏠 🐗⚔️Prinz Valium VI ⚔️🐗 [232] l+k://coordinates?16464,16341&230
🏠 🐗⚔️Ballindaloch⚔️🐗 [268] l+k://coordinates?16459,16341&230
🏠 🐗⚔️Findhorn⚔️🐗 [264] l+k://coordinates?16465,16341&230
🏠 Ex-Artur [289] l+k://coordinates?16433,16377&230
🏠 🐗⚔️BD 15⚔️🐗 [253] l+k://coordinates?16445,16354&230
🏠 3.8k 🐗⚔️Ty Gwynn 05⚔️🐗 [266] l+k://coordinates?16430,16381&230
🏠 3k 🐗⚔️Ty Gwynn 02⚔️🐗 [254] l+k://coordinates?16429,16383&230
🏠 🐗⚔️Winterfell1️⃣3️⃣⚔️🐗 [278] l+k://coordinates?16432,16390&230
🏠 🐗⚔️Winterfell1️⃣2️⃣⚔️🐗 [278] l+k://coordinates?16431,16388&230
🏠 🐗⚔️Winterfell2️⃣0️⃣⚔️🐗 [262] l+k://coordinates?16431,16380&230
🏠 🐗⚔️Winterfell0️⃣3️⃣⚔️🐗 [279] l+k://coordinates?16431,16389&230
🏠 ｬཞ ✞ ཀ Σ 🐒007 [275] l+k://coordinates?16438,16365&230
🏠 ｬཞ ✞ ཀ Σ 🐒005 [275] l+k://coordinates?16439,16364&230
🏠 🐗⚔️006 Burg⚔️🐗 [254] l+k://coordinates?16464,16340&230
🏠 🐗⚔️Cawdor⚔️🐗 [266] l+k://coordinates?16459,16340&230
🏠 🐗⚔️Eilean Donan⚔️🐗 [269] l+k://coordinates?16458,16340&230
🏠 🐗⚔️MacLachlan⚔️🐗 [263] l+k://coordinates?16461,16340&230
🏠 🐗⚔️BD 19-1⚔️🐗 [223] l+k://coordinates?16445,16351&230
🏠 🐗⚔️Ty Gwynn 12⚔️🐗 [263] l+k://coordinates?16452,16339&230
🏠 4.5k 🐗⚔️Ty Gwynn 01 ⚔️🐗 [259] l+k://coordinates?16428,16383&230
🏠 2.2k 🐗⚔️Ty Gwynn 03⚔️🐗 [255] l+k://coordinates?16429,16381&230
🏠 ｬཞ ✞ ཀ Σ 🐒011 [274] l+k://coordinates?16437,16365&230
🏠 Ex- Roastbeef 02🎉 [277] l+k://coordinates?16430,16379&230
🏠 🐗⚔️ FS 🗿P01 ⚔️🐗 [216] l+k://coordinates?16455,16339&230
🏠 🐗⚔️Himmel022⚔️🐗 [208] l+k://coordinates?16436,16367&230
🏠 🐗⚔️007 Burg⚔️🐗 [259] l+k://coordinates?16462,16339&230
🏠 🐗⚔️Kinnaird⚔️🐗 [263] l+k://coordinates?16458,16339&230
🏠 🐗⚔️BD 19⚔️🐗 [222] l+k://coordinates?16444,16351&230
🏠 ｬཞ ✞ ཀ Σ 🐒009 [275] l+k://coordinates?16438,16361&230
🏠 ｬཞ ✞ ཀ Σ 🐒013 [276] l+k://coordinates?16439,16360&230
🏠 🐗⚔️ FS 🗿P0⚔️🐗 [230] l+k://coordinates?16454,16338&230
🏠 🐗⚔️FS🧟‍♂️ 01⚔️🐗 [219] l+k://coordinates?16449,16339&230
🏠 🐗⚔️ FS 🗿P02 ⚔️🐗 [203] l+k://coordinates?16455,16338&230
🏠 🐗⚔️004 Burg⚔️🐗 [260] l+k://coordinates?16464,16338&230
🏠 🐗⚔️001 Burg⚔️🐗 [269] l+k://coordinates?16466,16338&230
🏠 🐗⚔️Fincharn⚔️🐗 [267] l+k://coordinates?16458,16338&230
🏠 🐗⚔️Forres⚔️🐗 [263] l+k://coordinates?16457,16338&230
🏠 🐗⚔️Drumduan⚔️🐗 [264] l+k://coordinates?16461,16338&230
🏠 Free Knight1337 [238] l+k://coordinates?16433,16371&230
🏠 🐗⚔️ Dunkelheit 02 ⚔️🐗 [250] l+k://coordinates?16446,16346&230
🏠 🐗⚔️ Dunkelheit 04 ⚔️🐗 [250] l+k://coordinates?16447,16344&230
🏠 🐗⚔️BD 17⚔️🐗 [218] l+k://coordinates?16441,16355&230
🏠 Free Knight30022 [286] l+k://coordinates?16427,16387&230
🏠 Free Knight8222 [255] l+k://coordinates?16451,16337&230
🏠 🐗⚔️Ty Gwynn 13⚔️🐗 [256] l+k://coordinates?16452,16337&230
🏠 🐗⚔️Winterfell0️⃣9️⃣⚔️🐗 [276] l+k://coordinates?16428,16389&230
🏠 LOCKDOWN [276] l+k://coordinates?16436,16364&230
🏠 Futternapf 09 [286] l+k://coordinates?16428,16379&230
🏠 🐗⚔️003 Burg⚔️🐗 [256] l+k://coordinates?16464,16337&230
🏠 🐗⚔️010 Burg⚔️🐗 [243] l+k://coordinates?16460,16337&230
🏠 🐗⚔️008 Burg⚔️🐗 [256] l+k://coordinates?16462,16337&230
🏠 🐗⚔️002 Burg⚔️🐗 [262] l+k://coordinates?16465,16337&230
🏠 🐗⚔️3🧟‍♂️⚔️🐗 [278] l+k://coordinates?16449,16338&230
🏠 Free Knight1304 [230] l+k://coordinates?16433,16369&230
🏠 🐗⚔️ Dunkelheit 01 ⚔️🐗 [252] l+k://coordinates?16446,16344&230
🏠 🐗⚔️ Dunkelheit 03 ⚔️🐗 [250] l+k://coordinates?16445,16346&230
🏠 🐗⚔️BD 16⚔️🐗 [239] l+k://coordinates?16439,16357&230
🏠 🐗⚔️BD 14⚔️🐗 [255] l+k://coordinates?16432,16371&230
🏠 🐗⚔️Snip 1⚔️🐗 [284] l+k://coordinates?16426,16386&230
🏠 🐗⚔️005 Burg⚔️🐗 [255] l+k://coordinates?16464,16336&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣8️⃣ [216] l+k://coordinates?16440,16354&230
🏠 🐗⚔️Pittlochry⚔️🐗 [263] l+k://coordinates?16458,16336&230
🏠 JETFIRE [289] l+k://coordinates?16436,16362&230
🏠 🐗⚔️1🧟‍♂️⚔️🐗 [281] l+k://coordinates?16449,16336&230
🏠 🐗⚔️ Dunkelheit 07 ⚔️🐗 [235] l+k://coordinates?16443,16347&230
🏠 🐗⚔️Snip 5⚔️🐗 [284] l+k://coordinates?16425,16386&230
🏠 🐗⚔️Snip 3⚔️🐗 [284] l+k://coordinates?16425,16387&230
🏠 🐗⚔️Prinz Valium I ⚔️🐗 [265] l+k://coordinates?16451,16335&230
🏠 🐗⚔️FS🧟‍♂️ 02⚔️🐗 [202] l+k://coordinates?16450,16335&230
🏠 Futternapf 12 [288] l+k://coordinates?16424,16385&230
🏠 🐗⚔️009 Burg⚔️🐗 [242] l+k://coordinates?16460,16335&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣2️⃣ [259] l+k://coordinates?16437,16357&230
🏠 Free Knight8181 [282] l+k://coordinates?16446,16340&230
🏠 🐗⚔️5🧟‍♂️⚔️🐗 [284] l+k://coordinates?16447,16337&230
🏠 🐗⚔️ Dunkelheit 05 ⚔️🐗 [247] l+k://coordinates?16443,16345&230
🏠 🏠 016 🏡 [281] l+k://coordinates?16430,16369&230
🏠 🏠 017 🏡 [270] l+k://coordinates?16428,16373&230
🏠 🐗⚔️ЅCHΔ∏ƘЅ⚔️🐗 [289] l+k://coordinates?16431,16368&230
🏠 🔱✊ HE PLU 0️⃣2️⃣ ✊🔱 [263] l+k://coordinates?16462,16334&230
🏠 🔱✊ HE PLU 0️⃣4️⃣ ✊🔱 [261] l+k://coordinates?16461,16334&230
🏠 🐗⚔️Prinz Valium X ⚔️🐗 [231] l+k://coordinates?16455,16334&230
🏠 🐗⚔️Prinz Valium IX ⚔️🐗 [233] l+k://coordinates?16457,16334&230
🏠 Futternapf 10 [287] l+k://coordinates?16427,16375&230
🏠 Futternapf 11 [287] l+k://coordinates?16424,16381&230
🏠 🦄 5 [272] l+k://coordinates?16441,16348&230
🏠 🐗⚔️020 Ex-Jay ⚔️🐗 [238] l+k://coordinates?16445,16340&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣1️⃣ [266] l+k://coordinates?16437,16356&230
🏠 🐗⚔️6🧟‍♂️⚔️🐗 [278] l+k://coordinates?16448,16334&230
🏠 🐗⚔️BD 11⚔️🐗 [264] l+k://coordinates?16437,16355&230
🏠 🏠 015 🏡 [278] l+k://coordinates?16429,16369&230
🏠 🏠 014 🏡 [272] l+k://coordinates?16428,16371&230
🏠 🔱✊ HE PLU 0️⃣6️⃣ [259] l+k://coordinates?16464,16333&230
🏠 🔱✊ HE PLU 0️⃣5️⃣ [259] l+k://coordinates?16463,16333&230
🏠 JAY0️⃣3️⃣ [245] l+k://coordinates?16447,16333&230
🏠 🐗⚔️Prinz Valium VIII ⚔️🐗 [231] l+k://coordinates?16457,16333&230
🏠 Futternapf 07 [288] l+k://coordinates?16428,16372&230
🏠 🐗⚔️021 Ex-Jay ⚔️🐗 [235] l+k://coordinates?16446,16336&230
🏠 🐗⚔️ ВͭіͪGͤ3️⃣1️⃣ [235] l+k://coordinates?16431,16366&230
🏠 🐗⚔️ Dunkelheit 06 ⚔️🐗 [245] l+k://coordinates?16441,16345&230
🏠 Free Knight8242 [254] l+k://coordinates?16453,16332&230
🏠 Milf 5 [287] l+k://coordinates?16429,16367&230
🏠 🏠 012 🏡 [273] l+k://coordinates?16428,16369&230
🏠 🔱✊ HE PLU 0️⃣1️⃣ ✊🔱 [269] l+k://coordinates?16462,16332&230
🏠 JAY1️⃣1️⃣ [227] l+k://coordinates?16448,16332&230
🏠 JAY0️⃣1️⃣ [285] l+k://coordinates?16445,16336&230
🏠 Futternapf 04 [225] l+k://coordinates?16427,16372&230
🏠 Futternapf 02 [286] l+k://coordinates?16426,16373&230
🏠 🦄 3 [277] l+k://coordinates?16439,16348&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣4️⃣ [283] l+k://coordinates?16423,16379&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣0️⃣ [289] l+k://coordinates?16433,16360&230
🏠 🐗⚔️Sarothorn P08⚔️🐗 [234] l+k://coordinates?16457,16331&230
🏠 🐗 ⚔️🌹03🌹⚔️🐗 [275] l+k://coordinates?16433,16358&230
🏠 🔱✊ HE PLU 0️⃣3️⃣ ✊🔱 [260] l+k://coordinates?16462,16331&230
🏠 🔱✊ HE FON 0️⃣0️⃣2️⃣ [278] l+k://coordinates?16420,16385&230
🏠 JAY0️⃣8️⃣ [231] l+k://coordinates?16443,16337&230
🏠 🐗⚔️Sarothorn P05⚔️🐗 [249] l+k://coordinates?16460,16331&230
🏠 JAY0️⃣7️⃣ [232] l+k://coordinates?16444,16336&230
🏠 🐗⚔️Sarothorn P01⚔️🐗 [257] l+k://coordinates?16458,16331&230
🏠 JAY0️⃣4️⃣ [282] l+k://coordinates?16445,16334&230
🏠 🐗⚔️Prinz Valium II ⚔️🐗 [256] l+k://coordinates?16456,16331&230
🏠 Futternapf 08 [287] l+k://coordinates?16426,16372&230
🏠 Futternapf 01 [288] l+k://coordinates?16426,16371&230
🏠 Futternapf 03 [284] l+k://coordinates?16427,16369&230
🏠 🦄 4 [274] l+k://coordinates?16439,16346&230
🏠 Frauenarzt [214] l+k://coordinates?16437,16350&230
🏠 🐗⚔️Sarothorn P03⚔️🐗 [255] l+k://coordinates?16459,16331&230
🏠 🐗⚔️Sarothorn P09⚔️🐗 [228] l+k://coordinates?16457,16330&230
🏠 ༺࿈ Kosmos Érimos ࿈༻ [280] l+k://coordinates?16419,16384&230
🏠 Ex- kuddel🎊 [289] l+k://coordinates?16454,16330&230
🏠 🐗⚔️Wesel1😎⚔️🐗 [223] l+k://coordinates?16431,16360&230
🏠 JAY0️⃣2️⃣ [286] l+k://coordinates?16445,16332&230
🏠 JAY1️⃣0️⃣ [231] l+k://coordinates?16445,16331&230
🏠 JAY0️⃣5️⃣ [286] l+k://coordinates?16444,16334&230
🏠 🦄 1 [288] l+k://coordinates?16437,16347&230
🏠 🦄 2 [275] l+k://coordinates?16437,16348&230
🏠 🦄 9 [242] l+k://coordinates?16434,16353&230
🏠 🦄 7 [261] l+k://coordinates?16435,16352&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣3️⃣ [282] l+k://coordinates?16421,16380&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣1️⃣ [260] l+k://coordinates?16429,16364&230
🏠 🐗⚔️Urquhart⚔️🐗 [265] l+k://coordinates?16453,16330&230
🏠 🐗⚔️Sarothorn P06⚔️🐗 [249] l+k://coordinates?16461,16330&230
🏠 Stepsister6 [263] l+k://coordinates?16423,16376&230
🏠 🐗⚔️1.05. Mag⚔️🐗 [277] l+k://coordinates?16435,16349&230
🏠 🐗⚔️1.04. Mag ⚔️🐗 [276] l+k://coordinates?16436,16348&230
🏠 🔱✊ HE PLU 0️⃣7️⃣ [235] l+k://coordinates?16462,16329&230
🏠 Pluviam B4.3 [280] l+k://coordinates?16443,16334&230
🏠 Pluviam B4.4 [283] l+k://coordinates?16442,16336&230
🏠 🦄 6 [269] l+k://coordinates?16434,16352&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣2️⃣ [214] l+k://coordinates?16427,16365&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣7️⃣ [271] l+k://coordinates?16429,16362&230
🏠 🐗⚔️Toreduff⚔️🐗 [264] l+k://coordinates?16454,16329&230
🏠 Rentnerbude 08 [205] l+k://coordinates?16463,16329&230
🏠 Rentnerbude 04 [230] l+k://coordinates?16465,16329&230
🏠 🐗⚔️Sarothorn P04⚔️🐗 [249] l+k://coordinates?16459,16329&230
🏠 🐗⚔️BD 20⚔️🐗 [285] l+k://coordinates?16419,16386&230
🏠 ༺࿈ Fons B1.5 Kosmos ࿈༻ [275] l+k://coordinates?16418,16387&230
🏠 🐗⚔️1.01. Mag ⚔️🐗 [278] l+k://coordinates?16436,16345&230
🏠 Pluviam B4.2 [278] l+k://coordinates?16442,16333&230
🏠 🐗⚔️Sarothorn P02⚔️🐗 [258] l+k://coordinates?16443,16331&230
🏠 Pluviam B4.1 [282] l+k://coordinates?16441,16335&230
🏠 Pluviam B3.3 [282] l+k://coordinates?16446,16328&230
🏠 Pluviam B4.5 [279] l+k://coordinates?16443,16332&230
🏠 Free Knight1697 [231] l+k://coordinates?16433,16352&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣4️⃣ [209] l+k://coordinates?16429,16359&230
🏠 🐗⚔️Y⚔️🐗 [266] l+k://coordinates?16455,16328&230
🏠 Rentnerbude 07 [206] l+k://coordinates?16465,16328&230
🏠 Rentnerbude 05 [207] l+k://coordinates?16464,16328&230
🏠 🐗⚔️Sarothorn P07⚔️🐗 [249] l+k://coordinates?16461,16328&230
🏠 🐗⚔️Sarothorn P10⚔️🐗 [213] l+k://coordinates?16457,16327&230
🏠 🐗⚔️Sarothorn P11⚔️🐗 [208] l+k://coordinates?16458,16327&230
🏠 ༺࿈Cas[a] Vacia🐒࿈༻ [277] l+k://coordinates?16452,16327&230
🏠 Geißbock 4 [276] l+k://coordinates?16424,16367&230
🏠 🐗⚔️1.02. Mag ⚔️🐗 [278] l+k://coordinates?16435,16345&230
🏠 🐗⚔️Asvlet 030⚔️🐗 [268] l+k://coordinates?16427,16361&230
🏠 Pluviam B3.4 [278] l+k://coordinates?16446,16327&230
🏠 Fons Burg geklaut [274] l+k://coordinates?16443,16330&230
🏠 FB 333-14 [203] l+k://coordinates?16416,16383&230
🏠 🦄 8 [256] l+k://coordinates?16433,16349&230
🏠 🐗⚔️011 Burg⚔️🐗 [230] l+k://coordinates?16462,16327&230
🏠 🐗⚔️012 Burg⚔️🐗 [231] l+k://coordinates?16463,16327&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣5️⃣ [289] l+k://coordinates?16432,16352&230
🏠 🐗⚔️ ВͭіͪGͤ3️⃣0️⃣ [245] l+k://coordinates?16434,16348&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣7️⃣ [263] l+k://coordinates?16428,16359&230
🏠 мαяɢαт [289] l+k://coordinates?16421,16373&230
🏠 тoυя яoυɢε [289] l+k://coordinates?16421,16374&230
🏠 Rentnerbude 06 [201] l+k://coordinates?16465,16327&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 005 [276] l+k://coordinates?16455,16326&230
🏠 Geißbock 2 [276] l+k://coordinates?16423,16367&230
🏠 Geißbock 1 [278] l+k://coordinates?16423,16368&230
🏠 Geißbock 15 [271] l+k://coordinates?16422,16370&230
🏠 Geißbock 7 [271] l+k://coordinates?16426,16362&230
🏠 🐗⚔Centurio9⚔🐗 [258] l+k://coordinates?16441,16332&230
🏠 🐗⚔Centurio11⚔🐗 [248] l+k://coordinates?16440,16334&230
🏠 🐗⚔️1.06. Mag🔥 ⚔️🐗 [271] l+k://coordinates?16436,16342&230
🏠 🐗⚔️1.03. Mag🔥 ⚔️🐗 [278] l+k://coordinates?16434,16345&230
🏠 🐗⚔️Asvlet 031⚔️🐗 [261] l+k://coordinates?16427,16360&230
🏠 🐗⚔️Asvlet 032⚔️🐗 [260] l+k://coordinates?16427,16359&230
🏠 Pluviam B3.1 [279] l+k://coordinates?16447,16326&230
🏠 Pluviam B2.1 [282] l+k://coordinates?16444,16326&230
🏠 FB 333-12 [210] l+k://coordinates?16415,16384&230
🏠 FB 333-11 [220] l+k://coordinates?16415,16383&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣2️⃣ [271] l+k://coordinates?16431,16352&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣8️⃣ [268] l+k://coordinates?16432,16349&230
🏠 cυяsαт [289] l+k://coordinates?16420,16373&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 006 [276] l+k://coordinates?16456,16325&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 004 [277] l+k://coordinates?16455,16325&230
🏠 ༺࿈Cas[a] Vacia࿈༻ [277] l+k://coordinates?16453,16325&230
🏠 Geißbock 11 [272] l+k://coordinates?16421,16370&230
🏠 🐗⚔Centurio3⚔🐗 [276] l+k://coordinates?16440,16332&230
🏠 🐗⚔Centurio2⚔🐗 [277] l+k://coordinates?16441,16329&230
🏠 🐗⚔️1.10. Mag⚔️🐗 [240] l+k://coordinates?16433,16345&230
🏠 🐗⚔️Asvlet 019⚔️🐗 [289] l+k://coordinates?16425,16362&230
🏠 Pluviam B2.3 [282] l+k://coordinates?16443,16326&230
🏠 Pluviam B2.2 [280] l+k://coordinates?16444,16325&230
🏠 Pluviam B5.2 [278] l+k://coordinates?16447,16325&230
🏠 FB 333-13 [207] l+k://coordinates?16415,16386&230
🏠 Free Knight1684 [205] l+k://coordinates?16431,16349&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣6️⃣ [268] l+k://coordinates?16429,16353&230
🏠 Andy [289] l+k://coordinates?16452,16325&230
🏠 Geißbock 9 [273] l+k://coordinates?16427,16356&230
🏠 🐗⚔Centurio22⚔🐗 [234] l+k://coordinates?16440,16329&230
🏠 🐗⚔Centurio12⚔🐗 [249] l+k://coordinates?16438,16333&230
🏠 🐗⚔️1.08. Mag ⚔️🐗 [241] l+k://coordinates?16433,16344&230
🏠 🐗⚔️1.09. Mag🔥 ⚔️🐗 [246] l+k://coordinates?16432,16345&230
🏠 🐗⚔️Asvlet 003⚔️🐗 [276] l+k://coordinates?16425,16359&230
🏠 Pluviam B2.4 [278] l+k://coordinates?16445,16324&230
🏠 Pluviam B5.1 [282] l+k://coordinates?16448,16324&230
🏠 11 Bernie🇺🇸Sanders [279] l+k://coordinates?16423,16364&230
🏠 🐗⚔️Himmel006⚔️🐗 [289] l+k://coordinates?16421,16368&230
🏠 Brazzers024 [285] l+k://coordinates?16423,16363&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣4️⃣ [267] l+k://coordinates?16428,16353&230
🏠 κεяακ [289] l+k://coordinates?16420,16370&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 001 [276] l+k://coordinates?16454,16323&230
🏠 🐗⚔️1.07. Mag ⚔️🐗 [256] l+k://coordinates?16432,16344&230
🏠 🐗⚔️Asvlet 010⚔️🐗 [259] l+k://coordinates?16423,16361&230
🏠 🐗⚔️Asvlet 012⚔️🐗 [282] l+k://coordinates?16424,16359&230
🏠 🐗⚔️Asvlet 002⚔️🐗 [278] l+k://coordinates?16425,16357&230
🏠 Pluviam B3.5 [281] l+k://coordinates?16445,16323&230
🏠 Free Knight8167 [285] l+k://coordinates?16442,16323&230
🏠 Pluviam B2.5 [278] l+k://coordinates?16443,16323&230
🏠 Pluviam B3.2 [281] l+k://coordinates?16446,16323&230
🏠 FB 333-15 [217] l+k://coordinates?16414,16388&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣9️⃣ [266] l+k://coordinates?16429,16350&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣9️⃣ [278] l+k://coordinates?16427,16354&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣6️⃣ [280] l+k://coordinates?16428,16352&230
🏠 🐗⚔️Pluviam002⚔️🐗 [289] l+k://coordinates?16460,16323&230
🏠 🐗⚔️Pluviam001⚔️🐗 [289] l+k://coordinates?16459,16323&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 007 [276] l+k://coordinates?16456,16322&230
🏠 Gustav [202] l+k://coordinates?16438,16329&230
🏠 🐗⚔️Asvlet 006⚔️🐗 [277] l+k://coordinates?16425,16355&230
🏠 🐗⚔️Asvlet 007⚔️🐗 [270] l+k://coordinates?16424,16358&230
🏠 Pluviam B5.5 [278] l+k://coordinates?16449,16322&230
🏠 Pluviam B5.3 [283] l+k://coordinates?16447,16322&230
🏠 01 Bernie🇺🇸Sanders [279] l+k://coordinates?16421,16363&230
🏠 🐗⚔️Doopey-06⚔️🐗 [204] l+k://coordinates?16465,16322&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣5️⃣ [285] l+k://coordinates?16426,16353&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣4️⃣ [286] l+k://coordinates?16427,16352&230
🏠 🐗⚔️ ВͭіͪGͤ⛓1️⃣0️⃣ [279] l+k://coordinates?16418,16369&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣0️⃣ [276] l+k://coordinates?16428,16349&230
🏠 🧚‍♂Kämpferburg🧚‍♂ [237] l+k://coordinates?16430,16346&230
🏠 🐗⚔️🇮🇪4🇬🇧⚔️🐗 [282] l+k://coordinates?16435,16335&230
🏠 🐗⚔️🅱️2️⃣0️⃣⚔️🐗 [233] l+k://coordinates?16458,16322&230
🏠 Brazzers004 [268] l+k://coordinates?16420,16366&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 002 [276] l+k://coordinates?16454,16321&230
🏠 🐗⚔️Ovilava 01⚔️🐗 [225] l+k://coordinates?16460,16321&230
🏠 🐗⚔️Asvlet 001⚔️🐗 [287] l+k://coordinates?16425,16353&230
🏠 🐗⚔️Asvlet 016⚔️🐗 [264] l+k://coordinates?16421,16362&230
🏠 🐗⚔️Asvlet 014⚔️🐗 [265] l+k://coordinates?16420,16363&230
🏠 🐗⚔️Asvlet 011⚔️🐗 [253] l+k://coordinates?16422,16359&230
🏠 Pluviam Ersatz 002 [279] l+k://coordinates?16439,16325&230
🏠 Pluviam B5.4 [284] l+k://coordinates?16447,16321&230
🏠 🐗⚔️Doopey-05⚔️🐗 [218] l+k://coordinates?16464,16321&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣3️⃣ [283] l+k://coordinates?16426,16351&230
🏠 🐗⚔️🇮🇪5🇬🇧⚔️🐗 [289] l+k://coordinates?16435,16334&230
🏠 🐗⚔️🇮🇪1🇬🇧⚔️🐗 [290] l+k://coordinates?16434,16336&230
🏠 🐗⚔️🅱️2️⃣6️⃣⚔️🐗 [229] l+k://coordinates?16456,16321&230
🏠 ✪  ᗩ ƒ ƒ ℮ 🐒 ✪ 003 [275] l+k://coordinates?16454,16320&230
🏠 🐗⚔️Ovilava⚔️🐗 [236] l+k://coordinates?16461,16320&230
🏠 🐗⚔️Asvlet 013⚔️🐗 [252] l+k://coordinates?16421,16359&230
🏠 🐗⚔️Asvlet 005⚔️🐗 [279] l+k://coordinates?16423,16355&230
🏠 🐗⚔️Asvlet 004⚔️🐗 [284] l+k://coordinates?16425,16352&230
🏠 noob [286] l+k://coordinates?16440,16321&230
🏠 Free Knight8164 [286] l+k://coordinates?16441,16320&230
🏠 🐗⚔️Doopey-04⚔️🐗 [225] l+k://coordinates?16465,16320&230
🏠 匚尺卂山凵爪爪 [232] l+k://coordinates?16469,16320&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣8️⃣ [278] l+k://coordinates?16427,16347&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣3️⃣ [269] l+k://coordinates?16427,16348&230
🏠 🐗⚔️🇮🇪3🇬🇧⚔️🐗 [282] l+k://coordinates?16434,16334&230
🏠 🐗⚔️Ovilava 02⚔️🐗 [207] l+k://coordinates?16461,16319&230
🏠 Fly [237] l+k://coordinates?16443,16319&230
🏠 🐗⚔️Asvlet 015⚔️🐗 [247] l+k://coordinates?16420,16359&230
🏠 🐗⚔️Asvlet 021⚔️🐗 [271] l+k://coordinates?16423,16354&230
🏠 🐗⚔️Asvlet 022⚔️🐗 [271] l+k://coordinates?16422,16356&230
🏠 Pluviam Ersatz 001 [278] l+k://coordinates?16438,16323&230
🏠 12 Bernie🇺🇸Sanders [279] l+k://coordinates?16429,16341&230
🏠 丨几丿乇Ҡㄒㄖ尺乇几ㄥㄖ̈丂乇尺 [235] l+k://coordinates?16467,16319&230
🏠 Pluviam Ostfront 1 [206] l+k://coordinates?16469,16319&230
🏠 🐗⚔️ ВͭіͪGͤ1️⃣1️⃣ [266] l+k://coordinates?16425,16350&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣2️⃣ [287] l+k://coordinates?16425,16349&230
🏠 🐗⚔️ ВͭіͪGͤ⛓0️⃣9️⃣ [250] l+k://coordinates?16419,16362&230
🏠 🐗⚔️🇮🇪2🇬🇧⚔️🐗 [283] l+k://coordinates?16433,16334&230
🏠 🐗⚔️🅱️2️⃣5️⃣⚔️🐗 [234] l+k://coordinates?16457,16319&230
🏠 🕊Temple☄️ [276] l+k://coordinates?16454,16318&230
🏠 Cob [217] l+k://coordinates?16444,16318&230
🏠 Joh [217] l+k://coordinates?16445,16318&230
🏠 Pee [236] l+k://coordinates?16446,16318&230
🏠 s.op.h [227] l+k://coordinates?16447,16318&230
🏠 Pluviam Ersatz 003 [284] l+k://coordinates?16439,16320&230
🏠 Pluviam Ersatz 004 [281] l+k://coordinates?16437,16323&230
🏠 07 Bernie🇺🇸Sanders [279] l+k://coordinates?16428,16341&230
🏠 卂Ҡㄒ丨ᐯ 乇丨丂尺ㄖ丂ㄒㄥㄖ̈丂乇尺 [240] l+k://coordinates?16468,16318&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣1️⃣ [289] l+k://coordinates?16425,16347&230
🏠 🐗⚔️Imperio 015⚔️🐗 [239] l+k://coordinates?16454,16317&230
🏠 🐗⚔️Imperio 016⚔️🐗 [233] l+k://coordinates?16455,16317&230
🏠 🏠 002 ⛺️ [273] l+k://coordinates?16456,16317&230
🏠 🏠 001 ⛺️ [275] l+k://coordinates?16457,16317&230
🏠 Point [243] l+k://coordinates?16443,16317&230
🏠 🐗⚔️Asvlet 024⚔️🐗 [236] l+k://coordinates?16419,16357&230
🏠 🐗⚔️Asvlet 008⚔️🐗 [273] l+k://coordinates?16422,16351&230
🏠 🐗⚔️Asvlet 020⚔️🐗 [279] l+k://coordinates?16420,16355&230
🏠 Pluviam Ersatz 006 [279] l+k://coordinates?16438,16320&230
🏠 09 Bernie🇺🇸Sanders [279] l+k://coordinates?16427,16342&230
🏠 08 Bernie🇺🇸Sanders [280] l+k://coordinates?16427,16341&230
🏠 Pluviam Ostfront 2 [201] l+k://coordinates?16470,16317&230
🏠 🐗⚔️ ВͭіͪGͤ0️⃣7️⃣ [282] l+k://coordinates?16423,16349&230
🏠 🐗⚔️ ВͭіͪGͤ⛓1️⃣1️⃣ [250] l+k://coordinates?16417,16361&230
🏠 hag [203] l+k://coordinates?16442,16316&230
🏠 🐗⚔️Asvlet 009⚔️🐗 [263] l+k://coordinates?16422,16349&230
🏠 Free Knight8152 [289] l+k://coordinates?16438,16317&230
🏠 Pluviam Ersatz 005 [280] l+k://coordinates?16437,16320&230
🏠 匚卂尺卂爪乃卂 丨几ㄒ乇几丂丨ᐯ [230] l+k://coordinates?16469,16316&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣1️⃣ [269] l+k://coordinates?16424,16345&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣3️⃣ [207] l+k://coordinates?16428,16338&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣2️⃣ [261] l+k://coordinates?16425,16344&230
🏠 🐗⚔️ ВͭіͪGͤ2️⃣3️⃣ [260] l+k://coordinates?16420,16353&230
🏠 🐗⚔️Imperio 014⚔️🐗 [233] l+k://coordinates?16453,16315&230
🏠 Geißbock 6 n [239] l+k://coordinates?16417,16358&230
🏠 Geißbock 3 n [244] l+k://coordinates?16417,16357&230
🏠 adr [216] l+k://coordinates?16447,16315&230
🏠 Ill [261] l+k://coordinates?16444,16315&230
🏠 Est [255] l+k://coordinates?16443,16315&230
🏠 Pab [256] l+k://coordinates?16445,16315&230
🏠 Karlogustav [263] l+k://coordinates?16440,16315&230
🏠 🐗⚔️klm #01⚔️🐗 [277] l+k://coordinates?16429,16334&230
🏠 🐗⚔️klm #13⚔️🐗 [228] l+k://coordinates?16429,16333&230
🏠 Ҡ凵卩千乇尺卩卂丂ㄒ乇 [229] l+k://coordinates?16467,16315&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣9️⃣ [246] l+k://coordinates?16425,16342&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣2️⃣ [219] l+k://coordinates?16426,16339&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣0️⃣ [224] l+k://coordinates?16426,16340&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣3️⃣ [260] l+k://coordinates?16423,16345&230
🏠 🐗⚔️Imperio 013⚔️🐗 [232] l+k://coordinates?16454,16314&230
🏠 🐗⚔️Imperio 002⚔️🐗 [276] l+k://coordinates?16461,16314&230
🏠 🐗⚔️Snip 4⚔️🐗 [285] l+k://coordinates?16418,16353&230
🏠 🐗⚔️🦉3.01.🦉⚔️🐗 [272] l+k://coordinates?16419,16352&230
🏠 Ta.-Er. [270] l+k://coordinates?16445,16314&230
🏠 pajo [203] l+k://coordinates?16442,16314&230
🏠 Highland Park [255] l+k://coordinates?16444,16314&230
🏠 Sto [255] l+k://coordinates?16446,16314&230
🏠 05 Bernie🇺🇸Sanders [273] l+k://coordinates?16415,16359&230
🏠 🐗⚔️Himmel008⚔️🐗 [224] l+k://coordinates?16419,16351&230
🏠 🐗⚔️klm #11⚔️🐗 [236] l+k://coordinates?16430,16330&230
🏠 🐗⚔️klm #20⚔️🐗 [224] l+k://coordinates?16457,16314&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣4️⃣ [263] l+k://coordinates?16423,16344&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣1️⃣ [224] l+k://coordinates?16425,16339&230
🏠 🐗⚔️Mara🐜⚔️🐗 P 2.01 [237] l+k://coordinates?16464,16314&230
🏠 🐗⚔️Imperio 001⚔️🐗 [279] l+k://coordinates?16461,16313&230
🏠 🐗⚔️Imperio 011⚔️🐗 [241] l+k://coordinates?16454,16313&230
🏠 🐗⚔️Imperio 009⚔️🐗 [261] l+k://coordinates?16459,16313&230
🏠 Burg 8191 [201] l+k://coordinates?16439,16313&230
🏠 Osgiliath [205] l+k://coordinates?16440,16313&230
🏠 10 Bernie🇺🇸Sanders [278] l+k://coordinates?16415,16358&230
🏠 🐗⚔️Himmel009⚔️🐗 [218] l+k://coordinates?16419,16350&230
🏠 🐗⚔️Himmel021⚔️🐗 [209] l+k://coordinates?16416,16355&230
🏠 🐗⚔️klm #12⚔️🐗 [233] l+k://coordinates?16429,16330&230
🏠 🐗⚔️klm #10⚔️🐗 [235] l+k://coordinates?16429,16329&230
🏠 🐗⚔️klm #16⚔️🐗 [220] l+k://coordinates?16427,16334&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣7️⃣ [269] l+k://coordinates?16423,16342&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣5️⃣ [262] l+k://coordinates?16422,16343&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣8️⃣ [225] l+k://coordinates?16423,16341&230
🏠 🐗⚔️ FB 16 ⚔️🐗 [223] l+k://coordinates?16426,16335&230
🏠 🐗⚔️Imperio 003⚔️🐗 [265] l+k://coordinates?16459,16312&230
🏠 🐗⚔️Imperio 012⚔️🐗 [224] l+k://coordinates?16454,16312&230
🏠 🐗⚔️Imperio 008⚔️🐗 [262] l+k://coordinates?16460,16312&230
🏠 fvw [218] l+k://coordinates?16442,16312&230
🏠 Wolvs Bau [227] l+k://coordinates?16446,16312&230
🏠 06 Bernie🇺🇸Sanders [281] l+k://coordinates?16415,16356&230
🏠 🐗⚔️Himmel007⚔️🐗 [236] l+k://coordinates?16418,16350&230
🏠 🐗⚔️015 Ex-Nilu⚔️🐗 [259] l+k://coordinates?16432,16322&230
🏠 🐗⚔️ ВͭіͪGͤ👣0️⃣6️⃣ [264] l+k://coordinates?16422,16342&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣6️⃣ [280] l+k://coordinates?16423,16339&230
🏠 🐗⚔️Imperio 005⚔️🐗 [251] l+k://coordinates?16460,16311&230
🏠 🐗⚔️Imperio 004⚔️🐗 [256] l+k://coordinates?16461,16311&230
🏠 Geißbock 19 [272] l+k://coordinates?16416,16352&230
🏠 Geißbock 20 [269] l+k://coordinates?16415,16353&230
🏠 🐗⚔Centurio15⚔🐗 [257] l+k://coordinates?16426,16332&230
🏠 🐗⚔Centurio16⚔🐗 [260] l+k://coordinates?16427,16330&230
🏠 🐗⚔Centurio7⚔🐗 [265] l+k://coordinates?16426,16331&230
🏠 kar [216] l+k://coordinates?16444,16311&230
🏠 preg [235] l+k://coordinates?16446,16311&230
🏠 🐗⚔️klm #15⚔️🐗 [215] l+k://coordinates?16427,16329&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣5️⃣ [214] l+k://coordinates?16424,16335&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣8️⃣ [211] l+k://coordinates?16423,16338&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣4️⃣ [230] l+k://coordinates?16425,16333&230
🏠 🐗⚔️ ВͭіͪGͤ👣1️⃣7️⃣ [212] l+k://coordinates?16422,16339&230
🏠 🐗⚔️MRay01⚔️🐗 [242] l+k://coordinates?16455,16311&230
🏠 🐗⚔️Imperio 007⚔️🐗 [260] l+k://coordinates?16462,16310&230
🏠 🐗⚔️Imperio 006⚔️🐗 [254] l+k://coordinates?16461,16310&230
🏠 🐗⚔Centurio8⚔🐗 [262] l+k://coordinates?16427,16328&230
🏠 🐗⚔Centurio5⚔🐗 [267] l+k://coordinates?16424,16333&230
🏠 🐗⚔️klm #110⚔️🐗 [241] l+k://coordinates?16429,16323&230
🏠 🔴 🐗⚔️ [256] l+k://coordinates?16413,16356&230
🏠 🐗⚔️ FB 17 ⚔️🐗 [220] l+k://coordinates?16421,16339&230
🏠 Titan 1.11 [220] l+k://coordinates?16423,16336&230
🏠 🐗⚔Centurio1⚔🐗 [275] l+k://coordinates?16427,16326&230
🏠 🐗⚔Centurio13⚔🐗 [254] l+k://coordinates?16427,16325&230
🏠 🐗⚔Centurio25⚔🐗 [239] l+k://coordinates?16428,16323&230
🏠 🐗⚔Centurio24⚔🐗 [246] l+k://coordinates?16428,16324&230
🏠 Burg 8223 [205] l+k://coordinates?16440,16309&230
🏠 03 Bernie🇺🇸Sanders [275] l+k://coordinates?16412,16356&230
🏠 04 Bernie🇺🇸Sanders [279] l+k://coordinates?16411,16357&230
🏠 🐗⚔️klm #18⚔️🐗 [231] l+k://coordinates?16429,16322&230
🏠 luc [254] l+k://coordinates?16429,16321&230
🏠 🐗⚔️ ВͭіͪGͤ👣⛓0️⃣1️⃣ [208] l+k://coordinates?16420,16340&230
🏠 Titan 1.05 [273] l+k://coordinates?16422,16336&230
🏠 🐗⚔Centurio6⚔🐗 [263] l+k://coordinates?16425,16328&230
🏠 Free Knight8371 [203] l+k://coordinates?16452,16308&230
🏠 🐗⚔Centurio 14⚔🐗 [256] l+k://coordinates?16425,16327&230
🏠 kit kat [239] l+k://coordinates?16430,16318&230
🏠 Titan 1.03 [253] l+k://coordinates?16423,16331&230
🏠 Titan 1.10 [222] l+k://coordinates?16424,16329&230
🏠 Titan 1.09 [249] l+k://coordinates?16422,16333&230
🏠 Alonia 01.003 [284] l+k://coordinates?16425,16326&230
🏠 02 Bernie🇺🇸Sanders [278] l+k://coordinates?16409,16358&230
🏠 🐗⚔️MRay05⚔️🐗 [203] l+k://coordinates?16456,16307&230
🏠 Titan 1.08 [270] l+k://coordinates?16422,16331&230
🏠 Titan 1.02 [253] l+k://coordinates?16421,16334&230
🏠 Titan 1.13 [223] l+k://coordinates?16419,16338&230
🏠 Titan 1.07 [259] l+k://coordinates?16423,16329&230
🏠 Titan 1.04 [272] l+k://coordinates?16421,16333&230
🏠 Titan 1.15 [218] l+k://coordinates?16418,16339&230
🏠 Titan 1.01 [273] l+k://coordinates?16420,16335&230
🏠 Burg 8226 [203] l+k://coordinates?16439,16306&230
🏠 🐗⚔️Asvlet 029⚔️🐗 [252] l+k://coordinates?16428,16317&230
🏠 🐗⚔️Asvlet 027⚔️🐗 [258] l+k://coordinates?16429,16315&230
🏠 🐗⚔️014 Ex-Prometheus⚔️🐗 [249] l+k://coordinates?16414,16346&230
🏠 Friedrich der Große [207] l+k://coordinates?16431,16311&230
🏠 🐗⚔️Arnhem⚔️🐗 [263] l+k://coordinates?16415,16344&230
🏠 🐗⚔️MRay02⚔️🐗 [243] l+k://coordinates?16456,16306&230
🏠 Titan 1.12 [219] l+k://coordinates?16418,16337&230
🏠 Alonia 01.015 [253] l+k://coordinates?16422,16327&230
🏠 Alonia 01.002 [287] l+k://coordinates?16423,16325&230
🏠 Alonia 01.018 [249] l+k://coordinates?16423,16326&230
🏠 Hörnleinsburg [245] l+k://coordinates?16430,16312&230
🏠 🐗⚔️Asvlet 028⚔️🐗 [253] l+k://coordinates?16427,16317&230
🏠 🐗⚔️Asvlet 018⚔️🐗 [239] l+k://coordinates?16424,16323&230
🏠 Titan 1.14 [215] l+k://coordinates?16418,16336&230
🏠 Titan 1.06 [270] l+k://coordinates?16420,16332&230
🏠 ༺査💀 ᏢᏒᏫ 0️⃣0️⃣8️⃣💀査༻ [269] l+k://coordinates?16411,16350&230
🏠 Alonia 01.017 [252] l+k://coordinates?16420,16329&230
🏠 Alonia 01.016 [255] l+k://coordinates?16421,16328&230
🏠 Alonia 01.001 [290] l+k://coordinates?16421,16327&230
🏠 🐗⚔️Centurio21⚔️🐗 [232] l+k://coordinates?16417,16336&230
🏠 🐗⚔️Centurio19⚔️🐗 [262] l+k://coordinates?16418,16334&230
🏠 ༺査💀 ᏢᏒᏫ 0️⃣0️⃣3️⃣💀査༻ [259] l+k://coordinates?16411,16347&230
🏠 🐗⚔️Asvlet 017⚔️🐗 [253] l+k://coordinates?16425,16320&230
🏠 🐗⚔️ FB 15 ⚔️🐗 [264] l+k://coordinates?16412,16345&230
🏠 Alonia 01.006 [284] l+k://coordinates?16422,16323&230
🏠 Alonia 01.011 [269] l+k://coordinates?16423,16321&230
🏠 Alonia 01.005 [285] l+k://coordinates?16423,16322&230
🏠 Nafplion 02.002 [249] l+k://coordinates?16413,16341&230
🏠 🐗⚔️Centurio18⚔️🐗 [262] l+k://coordinates?16418,16332&230
🏠 🐗⚔Centurio23⚔🐗 [231] l+k://coordinates?16417,16334&230
🏠 ༺査💀 ᏢᏒᏫ 0️⃣0️⃣1️⃣💀査༻ [283] l+k://coordinates?16411,16345&230
🏠 Wartburg [251] l+k://coordinates?16427,16314&230
🏠 🐗⚔️Asvlet 023⚔️🐗 [206] l+k://coordinates?16425,16318&230
🏠 Feldmarschall v. Mannstein [210] l+k://coordinates?16429,16310&230
🏠 Alonia 01.019 [244] l+k://coordinates?16419,16327&230
🏠 Alonia 01.004 [285] l+k://coordinates?16419,16328&230
🏠 Alonia 01.007 [278] l+k://coordinates?16421,16324&230
🏠 Nafplion 02.001 [274] l+k://coordinates?16412,16341&230
🏠 🐗⚔️Centurio17⚔️🐗 [261] l+k://coordinates?16416,16333&230
🏠 🐗⚔️Centurio20⚔️🐗 [239] l+k://coordinates?16417,16332&230
🏠 Alonia 01.008 [276] l+k://coordinates?16419,16325&230
🏠 Alonia 01.012 [258] l+k://coordinates?16415,16334&230
🏠 Schloss Friedenstein [238] l+k://coordinates?16426,16312&230
🏠 Graf Hellmuth v. Moltke [240] l+k://coordinates?16427,16309&230
🏠 Alonia 01.020 [222] l+k://coordinates?16416,16329&230
🏠 Alonia 01.013 [254] l+k://coordinates?16417,16328&230
🏠 Mühlburg [212] l+k://coordinates?16424,16313&230
🏠 Erfurter Dom [207] l+k://coordinates?16425,16311&230
🏠 Burg Gleichen [242] l+k://coordinates?16425,16312&230
🏠 🐗⚔️klm #05⚔️🐗 [250] l+k://coordinates?16412,16337&230
🏠 Alonia 01.030 [283] l+k://coordinates?16417,16326&230
🏠 Alonia 01.010 [262] l+k://coordinates?16414,16331&230
🏠 Alonia 01.009 [274] l+k://coordinates?16415,16330&230
🏠 Alonia 01.014 [254] l+k://coordinates?16416,16327&230
🏠 Heidecksburg [242] l+k://coordinates?16427,16305&230
🏠 Alonia 01.021 [209] l+k://coordinates?16413,16332&230
🏠 Schaumburg [266] l+k://coordinates?16426,16306&230
🏠 Burg Rauenstein [249] l+k://coordinates?16425,16308&230
🏠 🐗⚔️klm #04⚔️🐗 [251] l+k://coordinates?16411,16336&230
🏠 🐗⚔️klm #03⚔️🐗 [253] l+k://coordinates?16410,16337&230
🏠 Alonia 01.029 [211] l+k://coordinates?16412,16332&230
🏠 Greifenstein [267] l+k://coordinates?16425,16305&230
🏠 Wasserburg Mitwitz [216] l+k://coordinates?16426,16304&230
🏠 🐗⚔️klm #02⚔️🐗 [260] l+k://coordinates?16410,16336&230
🏠 Alonia 01.028 [213] l+k://coordinates?16411,16332&230
🏠 Burg zu Eisfeld [251] l+k://coordinates?16424,16306&230
🏠 1|3|017 [270] l+k://coordinates?16406,16339&230
🏠 Dulli [288] l+k://coordinates?16352,16388&230
🏠 🐗⚔️Langer 1⚔️🐗P [233] l+k://coordinates?16547,16275&230
🏰 Free Knight17286 [1681] l+k://coordinates?16439,16292&230
🏰 Free Knight17198 [1636] l+k://coordinates?16434,16294&230
🏰 Festung 17305 [1754] l+k://coordinates?16441,16294&230
🏰 Free Knight17320 [1680] l+k://coordinates?16443,16298&230
🏰 Free Knight17330 [1684] l+k://coordinates?16443,16300&230
🏰 Festung 17329 [1755] l+k://coordinates?16443,16301&230
🏰 Free Knight17357 [1689] l+k://coordinates?16447,16298&230
🏰 S.H. [1642] l+k://coordinates?16443,16308&230
🏰 Festung 17340 [1629] l+k://coordinates?16442,16303&230
🏰 3.5k Freie Festung 17368 [1596] l+k://coordinates?16445,16303&230
🏰 ☀️ Till this Day 👊 3 ☀️ [1587] l+k://coordinates?16440,16381&230
🏰 ☀️ Till this Day 👊 2 ☀️ [1592] l+k://coordinates?16442,16382&230
🏰 Pluviam F1.2 [1615] l+k://coordinates?16445,16328&230
🏰 Pluviam F1.1 [1618] l+k://coordinates?16444,16329&230
"""
lines = big.split("\n")
random.shuffle(lines)
counter = 0
for line in lines:
    counter += 1
    if counter == 25:
        print("<><><><><><><><><><><><>")
        counter = 0
    print(line)