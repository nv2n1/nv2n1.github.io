---
title: "brlapi_keycode_t(3)"
name: "brlapi_keycode_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_keycode_t/"
description: "Types and Defines fore BrlAPI Key Codes –"
---

<p>Types and Defines fore BrlAPI Key Codes &#8211; </p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_PRIxKEYCODE</code> PRIx64 </p>
<p> #define <code>BRLAPI_PRIuKEYCODE</code> PRIu64 </p>
<p> #define <code>BRLAPI_KEY_MAX</code> UINT64_C(0XFFFFFFFFFFFFFFFF) </p>
<p> #define <code>BRLAPI_KEY_FLAGS_MASK</code> UINT64_C(0XFFFFFFFF00000000) </p>
<p> #define <code>BRLAPI_KEY_FLAGS_SHIFT</code> 32 </p>
<p> #define <code>BRLAPI_KEY_FLG</code>(v) ((<code>brlapi_keyCode_t</code>)(v) &lt;&lt; <code>BRLAPI_KEY_FLAGS_SHIFT</code>) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD1</code> <code>BRLAPI_KEY_FLG</code>(0x00000008) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD2</code> <code>BRLAPI_KEY_FLG</code>(0x00000010) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD3</code> <code>BRLAPI_KEY_FLG</code>(0x00000020) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD4</code> <code>BRLAPI_KEY_FLG</code>(0x00000040) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD5</code> <code>BRLAPI_KEY_FLG</code>(0x00000080) </p>
<p> #define <code>BRLAPI_KEY_TYPE_MASK</code> UINT64_C(0X00000000E0000000) </p>
<p> #define <code>BRLAPI_KEY_TYPE_SHIFT</code> 29 </p>
<p> #define <code>BRLAPI_KEY_TYPE_CMD</code> UINT64_C(0X0000000020000000) </p>
<p> #define <code>BRLAPI_KEY_TYPE_SYM</code> UINT64_C(0X0000000000000000) </p>
<p> #define <code>BRLAPI_KEY_CODE_MASK</code> UINT64_C(0X000000001FFFFFFF) </p>
<p> #define <code>BRLAPI_KEY_CODE_SHIFT</code> 0 </p>
<p> #define <code>BRLAPI_KEY_CMD_BLK_MASK</code> UINT64_C(0X1FFF0000) </p>
<p> #define <code>BRLAPI_KEY_CMD_BLK_SHIFT</code> 16 </p>
<p> #define <code>BRLAPI_KEY_CMD_ARG_MASK</code> UINT64_C(0X0000FFFF) </p>
<p> #define <code>BRLAPI_KEY_CMD_ARG_SHIFT</code> 0 </p>
<p> #define <code>BRLAPI_KEY_CMD</code>(v) ((v) &lt;&lt; <code>BRLAPI_KEY_CMD_BLK_SHIFT</code>) </p>
<p> #define <code>BRLAPI_KEY_SYM_BACKSPACE</code> UINT64_C(0X0000FF08) </p>
<p> #define <code>BRLAPI_KEY_SYM_TAB</code> UINT64_C(0X0000FF09) </p>
<p> #define <code>BRLAPI_KEY_SYM_LINEFEED</code> UINT64_C(0X0000FF0D) </p>
<p> #define <code>BRLAPI_KEY_SYM_ESCAPE</code> UINT64_C(0X0000FF1B) </p>
<p> #define <code>BRLAPI_KEY_SYM_HOME</code> UINT64_C(0X0000FF50) </p>
<p> #define <code>BRLAPI_KEY_SYM_LEFT</code> UINT64_C(0X0000FF51) </p>
<p> #define <code>BRLAPI_KEY_SYM_UP</code> UINT64_C(0X0000FF52) </p>
<p> #define <code>BRLAPI_KEY_SYM_RIGHT</code> UINT64_C(0X0000FF53) </p>
<p> #define <code>BRLAPI_KEY_SYM_DOWN</code> UINT64_C(0X0000FF54) </p>
<p> #define <code>BRLAPI_KEY_SYM_PAGE_UP</code> UINT64_C(0X0000FF55) </p>
<p> #define <code>BRLAPI_KEY_SYM_PAGE_DOWN</code> UINT64_C(0X0000FF56) </p>
<p> #define <code>BRLAPI_KEY_SYM_END</code> UINT64_C(0X0000FF57) </p>
<p> #define <code>BRLAPI_KEY_SYM_INSERT</code> UINT64_C(0X0000FF63) </p>
<p> #define <code>BRLAPI_KEY_SYM_FUNCTION</code> UINT64_C(0X0000FFBE) </p>
<p> #define <code>BRLAPI_KEY_SYM_DELETE</code> UINT64_C(0X0000FFFF) </p>
<p> #define <code>BRLAPI_KEY_SYM_UNICODE</code> UINT64_C(0X01000000) </p>
<h3>Typedefs</h3>
<p>typedef uint64_t <code>brlapi_keyCode_t</code> </p>
<p> #define <code>BRLAPI_KEY_CMD_NOOP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 0) </p>
<p> #define <code>BRLAPI_KEY_CMD_LNUP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 1) </p>
<p> #define <code>BRLAPI_KEY_CMD_LNDN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 2) </p>
<p> #define <code>BRLAPI_KEY_CMD_WINUP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 3) </p>
<p> #define <code>BRLAPI_KEY_CMD_WINDN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 4) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRDIFLN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 5) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXDIFLN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 6) </p>
<p> #define <code>BRLAPI_KEY_CMD_ATTRUP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 7) </p>
<p> #define <code>BRLAPI_KEY_CMD_ATTRDN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 8) </p>
<p> #define <code>BRLAPI_KEY_CMD_TOP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 9) </p>
<p> #define <code>BRLAPI_KEY_CMD_BOT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 10) </p>
<p> #define <code>BRLAPI_KEY_CMD_TOP_LEFT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 11) </p>
<p> #define <code>BRLAPI_KEY_CMD_BOT_LEFT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 12) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRPGRPH</code> (<code>BRLAPI_KEY_CMD</code>(0) + 13) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXPGRPH</code> (<code>BRLAPI_KEY_CMD</code>(0) + 14) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRPROMPT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 15) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXPROMPT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 16) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRSEARCH</code> (<code>BRLAPI_KEY_CMD</code>(0) + 17) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXSEARCH</code> (<code>BRLAPI_KEY_CMD</code>(0) + 18) </p>
<p> #define <code>BRLAPI_KEY_CMD_CHRLT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 19) </p>
<p> #define <code>BRLAPI_KEY_CMD_CHRRT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 20) </p>
<p> #define <code>BRLAPI_KEY_CMD_HWINLT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 21) </p>
<p> #define <code>BRLAPI_KEY_CMD_HWINRT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 22) </p>
<p> #define <code>BRLAPI_KEY_CMD_FWINLT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 23) </p>
<p> #define <code>BRLAPI_KEY_CMD_FWINRT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 24) </p>
<p> #define <code>BRLAPI_KEY_CMD_FWINLTSKIP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 25) </p>
<p> #define <code>BRLAPI_KEY_CMD_FWINRTSKIP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 26) </p>
<p> #define <code>BRLAPI_KEY_CMD_LNBEG</code> (<code>BRLAPI_KEY_CMD</code>(0) + 27) </p>
<p> #define <code>BRLAPI_KEY_CMD_LNEND</code> (<code>BRLAPI_KEY_CMD</code>(0) + 28) </p>
<p> #define <code>BRLAPI_KEY_CMD_HOME</code> (<code>BRLAPI_KEY_CMD</code>(0) + 29) </p>
<p> #define <code>BRLAPI_KEY_CMD_BACK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 30) </p>
<p> #define <code>BRLAPI_KEY_CMD_RETURN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 31) </p>
<p> #define <code>BRLAPI_KEY_CMD_FREEZE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 32) </p>
<p> #define <code>BRLAPI_KEY_CMD_DISPMD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 33) </p>
<p> #define <code>BRLAPI_KEY_CMD_SIXDOTS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 34) </p>
<p> #define <code>BRLAPI_KEY_CMD_SLIDEWIN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 35) </p>
<p> #define <code>BRLAPI_KEY_CMD_SKPIDLNS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 36) </p>
<p> #define <code>BRLAPI_KEY_CMD_SKPBLNKWINS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 37) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRVIS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 38) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRHIDE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 39) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRTRK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 40) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRSIZE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 41) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRBLINK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 42) </p>
<p> #define <code>BRLAPI_KEY_CMD_ATTRVIS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 43) </p>
<p> #define <code>BRLAPI_KEY_CMD_ATTRBLINK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 44) </p>
<p> #define <code>BRLAPI_KEY_CMD_CAPBLINK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 45) </p>
<p> #define <code>BRLAPI_KEY_CMD_TUNES</code> (<code>BRLAPI_KEY_CMD</code>(0) + 46) </p>
<p> #define <code>BRLAPI_KEY_CMD_AUTOREPEAT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 47) </p>
<p> #define <code>BRLAPI_KEY_CMD_AUTOSPEAK</code> (<code>BRLAPI_KEY_CMD</code>(0) + 48) </p>
<p> #define <code>BRLAPI_KEY_CMD_HELP</code> (<code>BRLAPI_KEY_CMD</code>(0) + 49) </p>
<p> #define <code>BRLAPI_KEY_CMD_INFO</code> (<code>BRLAPI_KEY_CMD</code>(0) + 50) </p>
<p> #define <code>BRLAPI_KEY_CMD_LEARN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 51) </p>
<p> #define <code>BRLAPI_KEY_CMD_PREFMENU</code> (<code>BRLAPI_KEY_CMD</code>(0) + 52) </p>
<p> #define <code>BRLAPI_KEY_CMD_PREFSAVE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 53) </p>
<p> #define <code>BRLAPI_KEY_CMD_PREFLOAD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 54) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_FIRST_ITEM</code> (<code>BRLAPI_KEY_CMD</code>(0) + 55) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_LAST_ITEM</code> (<code>BRLAPI_KEY_CMD</code>(0) + 56) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_PREV_ITEM</code> (<code>BRLAPI_KEY_CMD</code>(0) + 57) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_NEXT_ITEM</code> (<code>BRLAPI_KEY_CMD</code>(0) + 58) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_PREV_SETTING</code> (<code>BRLAPI_KEY_CMD</code>(0) + 59) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_NEXT_SETTING</code> (<code>BRLAPI_KEY_CMD</code>(0) + 60) </p>
<p> #define <code>BRLAPI_KEY_CMD_MUTE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 61) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPKHOME</code> (<code>BRLAPI_KEY_CMD</code>(0) + 62) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 63) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_ABOVE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 64) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_BELOW</code> (<code>BRLAPI_KEY_CMD</code>(0) + 65) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_SLOWER</code> (<code>BRLAPI_KEY_CMD</code>(0) + 66) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_FASTER</code> (<code>BRLAPI_KEY_CMD</code>(0) + 67) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_SOFTER</code> (<code>BRLAPI_KEY_CMD</code>(0) + 68) </p>
<p> #define <code>BRLAPI_KEY_CMD_SAY_LOUDER</code> (<code>BRLAPI_KEY_CMD</code>(0) + 69) </p>
<p> #define <code>BRLAPI_KEY_CMD_SWITCHVT_PREV</code> (<code>BRLAPI_KEY_CMD</code>(0) + 70) </p>
<p> #define <code>BRLAPI_KEY_CMD_SWITCHVT_NEXT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 71) </p>
<p> #define <code>BRLAPI_KEY_CMD_CSRJMP_VERT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 72) </p>
<p> #define <code>BRLAPI_KEY_CMD_PASTE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 73) </p>
<p> #define <code>BRLAPI_KEY_CMD_RESTARTBRL</code> (<code>BRLAPI_KEY_CMD</code>(0) + 74) </p>
<p> #define <code>BRLAPI_KEY_CMD_RESTARTSPEECH</code> (<code>BRLAPI_KEY_CMD</code>(0) + 75) </p>
<p> #define <code>BRLAPI_KEY_CMD_OFFLINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 76) </p>
<p> #define <code>BRLAPI_KEY_CMD_SHIFT</code> (<code>BRLAPI_KEY_CMD</code>(0) + 77) </p>
<p> #define <code>BRLAPI_KEY_CMD_UPPER</code> (<code>BRLAPI_KEY_CMD</code>(0) + 78) </p>
<p> #define <code>BRLAPI_KEY_CMD_CONTROL</code> (<code>BRLAPI_KEY_CMD</code>(0) + 79) </p>
<p> #define <code>BRLAPI_KEY_CMD_META</code> (<code>BRLAPI_KEY_CMD</code>(0) + 80) </p>
<p> #define <code>BRLAPI_KEY_CMD_TIME</code> (<code>BRLAPI_KEY_CMD</code>(0) + 81) </p>
<p> #define <code>BRLAPI_KEY_CMD_MENU_PREV_LEVEL</code> (<code>BRLAPI_KEY_CMD</code>(0) + 82) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_SEL_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 83) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_SEL_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 84) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_INS_CHARS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 85) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_DEL_CHARS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 86) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_REP_CHARS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 87) </p>
<p> #define <code>BRLAPI_KEY_CMD_ASPK_CMP_WORDS</code> (<code>BRLAPI_KEY_CMD</code>(0) + 88) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_CURR_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 89) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_PREV_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 90) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_NEXT_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 91) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_CURR_WORD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 92) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_PREV_WORD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 93) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_NEXT_WORD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 94) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_CURR_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 95) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_PREV_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 96) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_NEXT_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 97) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_FRST_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 98) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_LAST_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 99) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_FRST_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 100) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_LAST_LINE</code> (<code>BRLAPI_KEY_CMD</code>(0) + 101) </p>
<p> #define <code>BRLAPI_KEY_CMD_DESC_CURR_CHAR</code> (<code>BRLAPI_KEY_CMD</code>(0) + 102) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPELL_CURR_WORD</code> (<code>BRLAPI_KEY_CMD</code>(0) + 103) </p>
<p> #define <code>BRLAPI_KEY_CMD_ROUTE_CURR_LOCN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 104) </p>
<p> #define <code>BRLAPI_KEY_CMD_SPEAK_CURR_LOCN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 105) </p>
<p> #define <code>BRLAPI_KEY_CMD_SHOW_CURR_LOCN</code> (<code>BRLAPI_KEY_CMD</code>(0) + 106) </p>
<p> #define <code>BRLAPI_KEY_FLG_TOGGLE_ON</code> <code>BRLAPI_KEY_FLG</code>(0X0100) </p>
<p> #define <code>BRLAPI_KEY_FLG_TOGGLE_OFF</code> <code>BRLAPI_KEY_FLG</code>(0X0200) </p>
<p> #define <code>BRLAPI_KEY_FLG_TOGGLE_MASK</code> (<code>BRLAPI_KEY_FLG_TOGGLE_ON</code> | <code>BRLAPI_KEY_FLG_TOGGLE_OFF</code>) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOTION_ROUTE</code> <code>BRLAPI_KEY_FLG</code>(0X0400) </p>
<p> #define <code>BRLAPI_KEY_FLG_REPEAT_INITIAL</code> <code>BRLAPI_KEY_FLG</code>(0X8000) </p>
<p> #define <code>BRLAPI_KEY_FLG_REPEAT_DELAY</code> <code>BRLAPI_KEY_FLG</code>(0X4000) </p>
<p> #define <code>BRLAPI_KEY_FLG_REPEAT_MASK</code> (<code>BRLAPI_KEY_FLG_REPEAT_INITIAL</code> | <code>BRLAPI_KEY_FLG_REPEAT_DELAY</code>) </p>
<p> #define <code>BRLAPI_KEY_CMD_ROUTE</code> <code>BRLAPI_KEY_CMD</code>(0X01) </p>
<p> #define <code>BRLAPI_KEY_CMD_CLIP_NEW</code> <code>BRLAPI_KEY_CMD</code>(0X02) </p>
<p> #define <code>BRLAPI_KEY_CMD_CUTBEGIN</code> <code>BRLAPI_KEY_CMD</code>(0X02) </p>
<p> #define <code>BRLAPI_KEY_CMD_CLIP_ADD</code> <code>BRLAPI_KEY_CMD</code>(0X03) </p>
<p> #define <code>BRLAPI_KEY_CMD_CUTAPPEND</code> <code>BRLAPI_KEY_CMD</code>(0X03) </p>
<p> #define <code>BRLAPI_KEY_CMD_COPY_RECT</code> <code>BRLAPI_KEY_CMD</code>(0X04) </p>
<p> #define <code>BRLAPI_KEY_CMD_CUTRECT</code> <code>BRLAPI_KEY_CMD</code>(0X04) </p>
<p> #define <code>BRLAPI_KEY_CMD_COPY_LINE</code> <code>BRLAPI_KEY_CMD</code>(0X05) </p>
<p> #define <code>BRLAPI_KEY_CMD_CUTLINE</code> <code>BRLAPI_KEY_CMD</code>(0X05) </p>
<p> #define <code>BRLAPI_KEY_CMD_SWITCHVT</code> <code>BRLAPI_KEY_CMD</code>(0X06) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRINDENT</code> <code>BRLAPI_KEY_CMD</code>(0X07) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXINDENT</code> <code>BRLAPI_KEY_CMD</code>(0X08) </p>
<p> #define <code>BRLAPI_KEY_CMD_DESCCHAR</code> <code>BRLAPI_KEY_CMD</code>(0X09) </p>
<p> #define <code>BRLAPI_KEY_CMD_SETLEFT</code> <code>BRLAPI_KEY_CMD</code>(0X0A) </p>
<p> #define <code>BRLAPI_KEY_CMD_SETMARK</code> <code>BRLAPI_KEY_CMD</code>(0X0B) </p>
<p> #define <code>BRLAPI_KEY_CMD_GOTOMARK</code> <code>BRLAPI_KEY_CMD</code>(0X0C) </p>
<p> #define <code>BRLAPI_KEY_CMD_GOTOLINE</code> <code>BRLAPI_KEY_CMD</code>(0X0D) </p>
<p> #define <code>BRLAPI_KEY_FLG_LINE_SCALED</code> <code>BRLAPI_KEY_FLG</code>(0X0100) </p>
<p> #define <code>BRLAPI_KEY_FLG_LINE_TOLEFT</code> <code>BRLAPI_KEY_FLG</code>(0X0200) </p>
<p> #define <code>BRLAPI_KEY_CMD_PRDIFCHAR</code> <code>BRLAPI_KEY_CMD</code>(0X0E) </p>
<p> #define <code>BRLAPI_KEY_CMD_NXDIFCHAR</code> <code>BRLAPI_KEY_CMD</code>(0X0F) </p>
<p> #define <code>BRLAPI_KEY_CMD_CLIP_COPY</code> <code>BRLAPI_KEY_CMD</code>(0X10) </p>
<p> #define <code>BRLAPI_KEY_CMD_COPYCHARS</code> <code>BRLAPI_KEY_CMD</code>(0X10) </p>
<p> #define <code>BRLAPI_KEY_CMD_CLIP_APPEND</code> <code>BRLAPI_KEY_CMD</code>(0X11) </p>
<p> #define <code>BRLAPI_KEY_CMD_APNDCHARS</code> <code>BRLAPI_KEY_CMD</code>(0X11) </p>
<p> #define <code>BRLAPI_KEY_CMD_PWGEN</code> <code>BRLAPI_KEY_CMD</code>(0X12) </p>
<p> #define <code>BRLAPI_KEY_CMD_PASSDOTS</code> <code>BRLAPI_KEY_CMD</code>(0X22) </p>
<p> #define <code>BRLAPI_KEY_FLG_SHIFT</code> <code>BRLAPI_KEY_FLG</code>(0X01) </p>
<p> #define <code>BRLAPI_KEY_FLG_UPPER</code> <code>BRLAPI_KEY_FLG</code>(0X02) </p>
<p> #define <code>BRLAPI_KEY_FLG_CONTROL</code> <code>BRLAPI_KEY_FLG</code>(0X04) </p>
<p> #define <code>BRLAPI_KEY_FLG_META</code> <code>BRLAPI_KEY_FLG</code>(0X08) </p>
<p> #define <code>BRLAPI_DOT1</code> 0001 </p>
<p> #define <code>BRLAPI_DOT2</code> 0002 </p>
<p> #define <code>BRLAPI_DOT3</code> 0004 </p>
<p> #define <code>BRLAPI_DOT4</code> 0010 </p>
<p> #define <code>BRLAPI_DOT5</code> 0020 </p>
<p> #define <code>BRLAPI_DOT6</code> 0040 </p>
<p> #define <code>BRLAPI_DOT7</code> 0100 </p>
<p> #define <code>BRLAPI_DOT8</code> 0200 </p>
<p> #define <code>BRLAPI_DOTC</code> 0400 </p>
<p> #define <code>BRLAPI_KEY_CMD_PASSAT</code> <code>BRLAPI_KEY_CMD</code>(0X23) </p>
<p> #define <code>BRLAPI_KEY_CMD_PASSXT</code> <code>BRLAPI_KEY_CMD</code>(0X24) </p>
<p> #define <code>BRLAPI_KEY_CMD_PASSPS2</code> <code>BRLAPI_KEY_CMD</code>(0X25) </p>
<p> #define <code>BRLAPI_KEY_FLG_KBD_RELEASE</code> <code>BRLAPI_KEY_FLG</code>(0X0100) </p>
<p> #define <code>BRLAPI_KEY_FLG_KBD_EMUL0</code> <code>BRLAPI_KEY_FLG</code>(0X0200) </p>
<p> #define <code>BRLAPI_KEY_FLG_KBD_EMUL1</code> <code>BRLAPI_KEY_FLG</code>(0X0400) </p>
<p> #define <code>BRLAPI_KEY_CMD_CONTEXT</code> <code>BRLAPI_KEY_CMD</code>(0X26) </p>
<p> #define <code>BRLAPI_DOTS</code>(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8) </p>
<p> #define <code>BRLAPI_DOT_CHORD</code> 256 </p>
<h2>Detailed Description</h2>
<p>Key codes are unsigned 64 bit integers. This 64-bit space is split into 3 parts: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>bits 63-32 (BRLAPI_KEY_FLAGS_MASK), flags: bits 39-32 are standard X modifiers (shift, control, meta, &#8230;). Other flags are used for some commands, see documentation of BRLAPI_KEY_FLG_* for their respective uses.</p>
<dt>&bull;</p>
<dd>bits 31-29 (BRLAPI_KEY_TYPE_MASK), key type: either BRLAPI_KEY_TYPE_CMD for braille commands, or BRLAPI_KEY_TYPE_SYM for standard X keysyms.</p>
<dt>&bull;</p>
<dd>bits 28-0 (BRLAPI_KEY_CODE_MASK), key code: for braille commands, see BRLAPI_KEY_CMD_* ; for standard X keysyms, this is the keysym value, see X11 documentation, a complete list is probably available on your system in /usr/include/X11/keysymdef.h</dl>
<p> The third part is itself split into two parts: a command number and a command value. The relative sizes of these parts vary according to the key type. </p>
<p> For a braille command, bits 28-16 (BRLAPI_KEY_CMD_BLK_MASK) hold the braille command number, while bits 15-0 (BRLAPI_KEY_CMD_ARG_MASK) hold the command value. </p>
<p> For a X keysym, if it is a unicode keysym (0x1uvwxyz), then the command number part is 0x1000000 and the value part is 0xuvwxyz. Else, the command part is held by bits 28-8 and the value part is held by bits 7-0. This permits to easily handle usual cases like 0x00xy (latin1), 0x01xy (latin2), XK_Backspace (0xff08, backspace), XK_Tab (0xff09, tab), &#8230; </p>
<p> For instance, if key == 0x0000000020010008,</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_TYPE_MASK) == BRLAPI_KEY_TYPE_CMD, so it&#8217;s a braille command</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_CMD_BLK_MASK) == BRLAPI_KEY_CMD_ROUTE, so it&#8217;s the braille route command.</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_CMD_ARG_MASK) == 8, so the highlighted cell is the 9th one (cells are numbered from 0)</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_FLAGS_MASK) == 0, so no modifier key was pressed during the command, and no particular flag applies to the command.</dl>
<p> if key == 0x000000010000FF09,</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_TYPE_MASK) == BRLAPI_KEY_TYPE_SYM, so it&#8217;s a keysym</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_CODE_MASK) == XK_Tab, so it&#8217;s the tab key. BRLAPI_KEY_SYM_TAB can also be used here, as well as a few other BRLAPI_KEY_SYM_* constants which are provided to avoid having to include X11/keysymdef.h</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_FLAGS_MASK) == BRLAPI_KEY_FLG_SHIFT, so the shift modifier was pressed during the command.</dl>
<p> in the X11 standard some keysyms are directly unicode, for instance if key == 0x0000000001001EA0,</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_TYPE_MASK) == BRLAPI_KEY_TYPE_SYM, so it&#8217;s a keysym</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_SYM_UNICODE) != 0 so it&#8217;s a unicode keysym, whose value is key &amp; (BRLAPI_KEY_SYM_UNICODE-1). Of course, one can also consider (key &amp; BRLAPI_KEY_CODE_MASK) == XK_Abelowdot</p>
<dt>&bull;</p>
<dd>(key &amp; BRLAPI_KEY_FLAGS_MASK) == 0, so no modifier key was pressed during the command, and no particular flag applies to the command.</dl>
<p> The <code>brlapi_expandKeyCode()</code> function may be used for splitting key codes into these parts.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_DOT1 0001</h3>
<p>upper-left dot of standard braille cell</p>
<h3>#define BRLAPI_DOT2 0002</h3>
<p>middle-left dot of standard braille cell</p>
<h3>#define BRLAPI_DOT3 0004</h3>
<p>lower-left dot of standard braille cell</p>
<h3>#define BRLAPI_DOT4 0010</h3>
<p>upper-right dot of standard braille cell</p>
<h3>#define BRLAPI_DOT5 0020</h3>
<p>middle-right dot of standard braille cell</p>
<h3>#define BRLAPI_DOT6 0040</h3>
<p>lower-right dot of standard braille cell</p>
<h3>#define BRLAPI_DOT7 0100</h3>
<p>lower-left dot of computer braille cell</p>
<h3>#define BRLAPI_DOT8 0200</h3>
<p>lower-right dot of computer braille cell</p>
<h3>#define BRLAPI_DOT_CHORD 256</h3>
<p>space key</p>
<h3>#define BRLAPI_DOTC 0400</h3>
<p>space key pressed</p>
<h3>#define BRLAPI_DOTS(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)</h3>
<p><code>Value:</code> </p>
<pre>( ((dot1)? BRLAPI_DOT1: 0) | ((dot2)? BRLAPI_DOT2: 0) | ((dot3)? BRLAPI_DOT3: 0) | ((dot4)? BRLAPI_DOT4: 0) | ((dot5)? BRLAPI_DOT5: 0) | ((dot6)? BRLAPI_DOT6: 0) | ((dot7)? BRLAPI_DOT7: 0) | ((dot8)? BRLAPI_DOT8: 0) )</pre>
<p>Helper macro to easily produce braille patterns</p>
<h3>#define BRLAPI_KEY_CMD(v) ((v) &lt;&lt; <code>BRLAPI_KEY_CMD_BLK_SHIFT</code>)</h3>
<h3>#define BRLAPI_KEY_CMD_APNDCHARS <code>BRLAPI_KEY_CMD</code>(0X11)</h3>
<p>deprecated definition of CLIP_APPEND &#8211; append characters to clipboard</p>
<h3>#define BRLAPI_KEY_CMD_ARG_MASK UINT64_C(0X0000FFFF)</h3>
<p>Mask for braille command value</p>
<h3>#define BRLAPI_KEY_CMD_ARG_SHIFT 0</h3>
<p>Shift for braille command value</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_CMP_WORDS (<code>BRLAPI_KEY_CMD</code>(0) + 88)</h3>
<p>set autospeak completed words on/off</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_DEL_CHARS (<code>BRLAPI_KEY_CMD</code>(0) + 86)</h3>
<p>set autospeak deleted characters on/off</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_INS_CHARS (<code>BRLAPI_KEY_CMD</code>(0) + 85)</h3>
<p>set autospeak inserted characters on/off</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_REP_CHARS (<code>BRLAPI_KEY_CMD</code>(0) + 87)</h3>
<p>set autospeak replaced characters on/off</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_SEL_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 84)</h3>
<p>set autospeak selected character on/off</p>
<h3>#define BRLAPI_KEY_CMD_ASPK_SEL_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 83)</h3>
<p>set autospeak selected line on/off</p>
<h3>#define BRLAPI_KEY_CMD_ATTRBLINK (<code>BRLAPI_KEY_CMD</code>(0) + 44)</h3>
<p>set attribute blinking on/off</p>
<h3>#define BRLAPI_KEY_CMD_ATTRDN (<code>BRLAPI_KEY_CMD</code>(0) + 8)</h3>
<p>go down to nearest line with different highlighting</p>
<h3>#define BRLAPI_KEY_CMD_ATTRUP (<code>BRLAPI_KEY_CMD</code>(0) + 7)</h3>
<p>go up to nearest line with different highlighting</p>
<h3>#define BRLAPI_KEY_CMD_ATTRVIS (<code>BRLAPI_KEY_CMD</code>(0) + 43)</h3>
<p>set attribute underlining on/off</p>
<h3>#define BRLAPI_KEY_CMD_AUTOREPEAT (<code>BRLAPI_KEY_CMD</code>(0) + 47)</h3>
<p>set autorepeat on/off</p>
<h3>#define BRLAPI_KEY_CMD_AUTOSPEAK (<code>BRLAPI_KEY_CMD</code>(0) + 48)</h3>
<p>set autospeak on/off</p>
<h3>#define BRLAPI_KEY_CMD_BACK (<code>BRLAPI_KEY_CMD</code>(0) + 30)</h3>
<p>go back after cursor tracking</p>
<h3>#define BRLAPI_KEY_CMD_BLK_MASK UINT64_C(0X1FFF0000)</h3>
<p>Mask for braille command type</p>
<h3>#define BRLAPI_KEY_CMD_BLK_SHIFT 16</h3>
<p>Shift for braille command type</p>
<h3>#define BRLAPI_KEY_CMD_BOT (<code>BRLAPI_KEY_CMD</code>(0) + 10)</h3>
<p>go to bottom line</p>
<h3>#define BRLAPI_KEY_CMD_BOT_LEFT (<code>BRLAPI_KEY_CMD</code>(0) + 12)</h3>
<p>go to beginning of bottom line</p>
<h3>#define BRLAPI_KEY_CMD_CAPBLINK (<code>BRLAPI_KEY_CMD</code>(0) + 45)</h3>
<p>set capital letter blinking on/off</p>
<h3>#define BRLAPI_KEY_CMD_CHRLT (<code>BRLAPI_KEY_CMD</code>(0) + 19)</h3>
<p>go left one character</p>
<h3>#define BRLAPI_KEY_CMD_CHRRT (<code>BRLAPI_KEY_CMD</code>(0) + 20)</h3>
<p>go right one character</p>
<h3>#define BRLAPI_KEY_CMD_CLIP_ADD <code>BRLAPI_KEY_CMD</code>(0X03)</h3>
<p>append to clipboard from character</p>
<h3>#define BRLAPI_KEY_CMD_CLIP_APPEND <code>BRLAPI_KEY_CMD</code>(0X11)</h3>
<p>append characters to clipboard</p>
<h3>#define BRLAPI_KEY_CMD_CLIP_COPY <code>BRLAPI_KEY_CMD</code>(0X10)</h3>
<p>copy characters to clipboard</p>
<h3>#define BRLAPI_KEY_CMD_CLIP_NEW <code>BRLAPI_KEY_CMD</code>(0X02)</h3>
<p>start new clipboard at character</p>
<h3>#define BRLAPI_KEY_CMD_CONTEXT <code>BRLAPI_KEY_CMD</code>(0X26)</h3>
<p>switch to command context</p>
<h3>#define BRLAPI_KEY_CMD_CONTROL (<code>BRLAPI_KEY_CMD</code>(0) + 79)</h3>
<p>set control modifier of next typed character or emulated key on/off</p>
<h3>#define BRLAPI_KEY_CMD_COPY_LINE <code>BRLAPI_KEY_CMD</code>(0X05)</h3>
<p>linear copy to character</p>
<h3>#define BRLAPI_KEY_CMD_COPY_RECT <code>BRLAPI_KEY_CMD</code>(0X04)</h3>
<p>rectangular copy to character</p>
<h3>#define BRLAPI_KEY_CMD_COPYCHARS <code>BRLAPI_KEY_CMD</code>(0X10)</h3>
<p>deprecated definition of CLIP_COPY &#8211; copy characters to clipboard</p>
<h3>#define BRLAPI_KEY_CMD_CSRBLINK (<code>BRLAPI_KEY_CMD</code>(0) + 42)</h3>
<p>set cursor blinking on/off</p>
<h3>#define BRLAPI_KEY_CMD_CSRHIDE (<code>BRLAPI_KEY_CMD</code>(0) + 39)</h3>
<p>set hidden cursor on/off</p>
<h3>#define BRLAPI_KEY_CMD_CSRJMP_VERT (<code>BRLAPI_KEY_CMD</code>(0) + 72)</h3>
<p>bring cursor to line</p>
<h3>#define BRLAPI_KEY_CMD_CSRSIZE (<code>BRLAPI_KEY_CMD</code>(0) + 41)</h3>
<p>set cursor style block/underline</p>
<h3>#define BRLAPI_KEY_CMD_CSRTRK (<code>BRLAPI_KEY_CMD</code>(0) + 40)</h3>
<p>set cursor tracking on/off</p>
<h3>#define BRLAPI_KEY_CMD_CSRVIS (<code>BRLAPI_KEY_CMD</code>(0) + 38)</h3>
<p>set cursor visibility on/off</p>
<h3>#define BRLAPI_KEY_CMD_CUTAPPEND <code>BRLAPI_KEY_CMD</code>(0X03)</h3>
<p>deprecated definition of CLIP_ADD &#8211; append to clipboard from character</p>
<h3>#define BRLAPI_KEY_CMD_CUTBEGIN <code>BRLAPI_KEY_CMD</code>(0X02)</h3>
<p>deprecated definition of CLIP_NEW &#8211; start new clipboard at character</p>
<h3>#define BRLAPI_KEY_CMD_CUTLINE <code>BRLAPI_KEY_CMD</code>(0X05)</h3>
<p>deprecated definition of COPY_LINE &#8211; linear copy to character</p>
<h3>#define BRLAPI_KEY_CMD_CUTRECT <code>BRLAPI_KEY_CMD</code>(0X04)</h3>
<p>deprecated definition of COPY_RECT &#8211; rectangular copy to character</p>
<h3>#define BRLAPI_KEY_CMD_DESC_CURR_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 102)</h3>
<p>describe current character</p>
<h3>#define BRLAPI_KEY_CMD_DESCCHAR <code>BRLAPI_KEY_CMD</code>(0X09)</h3>
<p>describe character</p>
<h3>#define BRLAPI_KEY_CMD_DISPMD (<code>BRLAPI_KEY_CMD</code>(0) + 33)</h3>
<p>set display mode attributes/text</p>
<h3>#define BRLAPI_KEY_CMD_FREEZE (<code>BRLAPI_KEY_CMD</code>(0) + 32)</h3>
<p>freeze/unfreeze screen image</p>
<h3>#define BRLAPI_KEY_CMD_FWINLT (<code>BRLAPI_KEY_CMD</code>(0) + 23)</h3>
<p>go left one window</p>
<h3>#define BRLAPI_KEY_CMD_FWINLTSKIP (<code>BRLAPI_KEY_CMD</code>(0) + 25)</h3>
<p>go left to nearest non-blank window</p>
<h3>#define BRLAPI_KEY_CMD_FWINRT (<code>BRLAPI_KEY_CMD</code>(0) + 24)</h3>
<p>go right one window</p>
<h3>#define BRLAPI_KEY_CMD_FWINRTSKIP (<code>BRLAPI_KEY_CMD</code>(0) + 26)</h3>
<p>go right to nearest non-blank window</p>
<h3>#define BRLAPI_KEY_CMD_GOTOLINE <code>BRLAPI_KEY_CMD</code>(0X0D)</h3>
<p>go to selected line</p>
<h3>#define BRLAPI_KEY_CMD_GOTOMARK <code>BRLAPI_KEY_CMD</code>(0X0C)</h3>
<p>go to remembered window position</p>
<h3>#define BRLAPI_KEY_CMD_HELP (<code>BRLAPI_KEY_CMD</code>(0) + 49)</h3>
<p>enter/leave help display</p>
<h3>#define BRLAPI_KEY_CMD_HOME (<code>BRLAPI_KEY_CMD</code>(0) + 29)</h3>
<p>go to cursor</p>
<h3>#define BRLAPI_KEY_CMD_HWINLT (<code>BRLAPI_KEY_CMD</code>(0) + 21)</h3>
<p>go left half a window</p>
<h3>#define BRLAPI_KEY_CMD_HWINRT (<code>BRLAPI_KEY_CMD</code>(0) + 22)</h3>
<p>go right half a window</p>
<h3>#define BRLAPI_KEY_CMD_INFO (<code>BRLAPI_KEY_CMD</code>(0) + 50)</h3>
<p>enter/leave status display</p>
<h3>#define BRLAPI_KEY_CMD_LEARN (<code>BRLAPI_KEY_CMD</code>(0) + 51)</h3>
<p>enter/leave command learn mode</p>
<h3>#define BRLAPI_KEY_CMD_LNBEG (<code>BRLAPI_KEY_CMD</code>(0) + 27)</h3>
<p>go to beginning of line</p>
<h3>#define BRLAPI_KEY_CMD_LNDN (<code>BRLAPI_KEY_CMD</code>(0) + 2)</h3>
<p>go down one line</p>
<h3>#define BRLAPI_KEY_CMD_LNEND (<code>BRLAPI_KEY_CMD</code>(0) + 28)</h3>
<p>go to end of line</p>
<h3>#define BRLAPI_KEY_CMD_LNUP (<code>BRLAPI_KEY_CMD</code>(0) + 1)</h3>
<p>go up one line</p>
<h3>#define BRLAPI_KEY_CMD_MENU_FIRST_ITEM (<code>BRLAPI_KEY_CMD</code>(0) + 55)</h3>
<p>go to first item</p>
<h3>#define BRLAPI_KEY_CMD_MENU_LAST_ITEM (<code>BRLAPI_KEY_CMD</code>(0) + 56)</h3>
<p>go to last item</p>
<h3>#define BRLAPI_KEY_CMD_MENU_NEXT_ITEM (<code>BRLAPI_KEY_CMD</code>(0) + 58)</h3>
<p>go to next item</p>
<h3>#define BRLAPI_KEY_CMD_MENU_NEXT_SETTING (<code>BRLAPI_KEY_CMD</code>(0) + 60)</h3>
<p>select next choice</p>
<h3>#define BRLAPI_KEY_CMD_MENU_PREV_ITEM (<code>BRLAPI_KEY_CMD</code>(0) + 57)</h3>
<p>go to previous item</p>
<h3>#define BRLAPI_KEY_CMD_MENU_PREV_LEVEL (<code>BRLAPI_KEY_CMD</code>(0) + 82)</h3>
<p>go to previous menu level</p>
<h3>#define BRLAPI_KEY_CMD_MENU_PREV_SETTING (<code>BRLAPI_KEY_CMD</code>(0) + 59)</h3>
<p>select previous choice</p>
<h3>#define BRLAPI_KEY_CMD_META (<code>BRLAPI_KEY_CMD</code>(0) + 80)</h3>
<p>set meta modifier of next typed character or emulated key on/off</p>
<h3>#define BRLAPI_KEY_CMD_MUTE (<code>BRLAPI_KEY_CMD</code>(0) + 61)</h3>
<p>stop speaking</p>
<h3>#define BRLAPI_KEY_CMD_NOOP (<code>BRLAPI_KEY_CMD</code>(0) + 0)</h3>
<p>do nothing</p>
<h3>#define BRLAPI_KEY_CMD_NXDIFCHAR <code>BRLAPI_KEY_CMD</code>(0X0F)</h3>
<p>go down to nearest line with different character</p>
<h3>#define BRLAPI_KEY_CMD_NXDIFLN (<code>BRLAPI_KEY_CMD</code>(0) + 6)</h3>
<p>go down to nearest line with different content</p>
<h3>#define BRLAPI_KEY_CMD_NXINDENT <code>BRLAPI_KEY_CMD</code>(0X08)</h3>
<p>go down to nearest line with less indent than character</p>
<h3>#define BRLAPI_KEY_CMD_NXPGRPH (<code>BRLAPI_KEY_CMD</code>(0) + 14)</h3>
<p>go down to first line of next paragraph</p>
<h3>#define BRLAPI_KEY_CMD_NXPROMPT (<code>BRLAPI_KEY_CMD</code>(0) + 16)</h3>
<p>go down to next command prompt</p>
<h3>#define BRLAPI_KEY_CMD_NXSEARCH (<code>BRLAPI_KEY_CMD</code>(0) + 18)</h3>
<p>search forward for clipboard text</p>
<h3>#define BRLAPI_KEY_CMD_OFFLINE (<code>BRLAPI_KEY_CMD</code>(0) + 76)</h3>
<p>braille display temporarily unavailable</p>
<h3>#define BRLAPI_KEY_CMD_PASSAT <code>BRLAPI_KEY_CMD</code>(0X23)</h3>
<p>AT (set 2) keyboard scan code</p>
<h3>#define BRLAPI_KEY_CMD_PASSDOTS <code>BRLAPI_KEY_CMD</code>(0X22)</h3>
<p>type braille character</p>
<h3>#define BRLAPI_KEY_CMD_PASSPS2 <code>BRLAPI_KEY_CMD</code>(0X25)</h3>
<p>PS/2 (set 3) keyboard scan code</p>
<h3>#define BRLAPI_KEY_CMD_PASSXT <code>BRLAPI_KEY_CMD</code>(0X24)</h3>
<p>XT (set 1) keyboard scan code</p>
<h3>#define BRLAPI_KEY_CMD_PASTE (<code>BRLAPI_KEY_CMD</code>(0) + 73)</h3>
<p>insert clipboard text at cursor</p>
<h3>#define BRLAPI_KEY_CMD_PRDIFCHAR <code>BRLAPI_KEY_CMD</code>(0X0E)</h3>
<p>go up to nearest line with different character</p>
<h3>#define BRLAPI_KEY_CMD_PRDIFLN (<code>BRLAPI_KEY_CMD</code>(0) + 5)</h3>
<p>go up to nearest line with different content</p>
<h3>#define BRLAPI_KEY_CMD_PREFLOAD (<code>BRLAPI_KEY_CMD</code>(0) + 54)</h3>
<p>restore preferences from disk</p>
<h3>#define BRLAPI_KEY_CMD_PREFMENU (<code>BRLAPI_KEY_CMD</code>(0) + 52)</h3>
<p>enter/leave preferences menu</p>
<h3>#define BRLAPI_KEY_CMD_PREFSAVE (<code>BRLAPI_KEY_CMD</code>(0) + 53)</h3>
<p>save preferences to disk</p>
<h3>#define BRLAPI_KEY_CMD_PRINDENT <code>BRLAPI_KEY_CMD</code>(0X07)</h3>
<p>go up to nearest line with less indent than character</p>
<h3>#define BRLAPI_KEY_CMD_PRPGRPH (<code>BRLAPI_KEY_CMD</code>(0) + 13)</h3>
<p>go up to last line of previous paragraph</p>
<h3>#define BRLAPI_KEY_CMD_PRPROMPT (<code>BRLAPI_KEY_CMD</code>(0) + 15)</h3>
<p>go up to previous command prompt</p>
<h3>#define BRLAPI_KEY_CMD_PRSEARCH (<code>BRLAPI_KEY_CMD</code>(0) + 17)</h3>
<p>search backward for clipboard text</p>
<h3>#define BRLAPI_KEY_CMD_PWGEN <code>BRLAPI_KEY_CMD</code>(0X12)</h3>
<p>put random password into clipboard</p>
<h3>#define BRLAPI_KEY_CMD_RESTARTBRL (<code>BRLAPI_KEY_CMD</code>(0) + 74)</h3>
<p>restart braille driver</p>
<h3>#define BRLAPI_KEY_CMD_RESTARTSPEECH (<code>BRLAPI_KEY_CMD</code>(0) + 75)</h3>
<p>restart speech driver</p>
<h3>#define BRLAPI_KEY_CMD_RETURN (<code>BRLAPI_KEY_CMD</code>(0) + 31)</h3>
<p>go to cursor or go back after cursor tracking</p>
<h3>#define BRLAPI_KEY_CMD_ROUTE <code>BRLAPI_KEY_CMD</code>(0X01)</h3>
<p>bring cursor to character</p>
<h3>#define BRLAPI_KEY_CMD_ROUTE_CURR_LOCN (<code>BRLAPI_KEY_CMD</code>(0) + 104)</h3>
<p>bring cursor to speech location</p>
<h3>#define BRLAPI_KEY_CMD_SAY_ABOVE (<code>BRLAPI_KEY_CMD</code>(0) + 64)</h3>
<p>speak from top of screen through current line</p>
<h3>#define BRLAPI_KEY_CMD_SAY_BELOW (<code>BRLAPI_KEY_CMD</code>(0) + 65)</h3>
<p>speak from current line through bottom of screen</p>
<h3>#define BRLAPI_KEY_CMD_SAY_FASTER (<code>BRLAPI_KEY_CMD</code>(0) + 67)</h3>
<p>increase speech rate</p>
<h3>#define BRLAPI_KEY_CMD_SAY_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 63)</h3>
<p>speak current line</p>
<h3>#define BRLAPI_KEY_CMD_SAY_LOUDER (<code>BRLAPI_KEY_CMD</code>(0) + 69)</h3>
<p>increase speech volume</p>
<h3>#define BRLAPI_KEY_CMD_SAY_SLOWER (<code>BRLAPI_KEY_CMD</code>(0) + 66)</h3>
<p>decrease speech rate</p>
<h3>#define BRLAPI_KEY_CMD_SAY_SOFTER (<code>BRLAPI_KEY_CMD</code>(0) + 68)</h3>
<p>decrease speech volume</p>
<h3>#define BRLAPI_KEY_CMD_SETLEFT <code>BRLAPI_KEY_CMD</code>(0X0A)</h3>
<p>place left end of window at character</p>
<h3>#define BRLAPI_KEY_CMD_SETMARK <code>BRLAPI_KEY_CMD</code>(0X0B)</h3>
<p>remember current window position</p>
<h3>#define BRLAPI_KEY_CMD_SHIFT (<code>BRLAPI_KEY_CMD</code>(0) + 77)</h3>
<p>set shift modifier of next typed character or emulated key on/off</p>
<h3>#define BRLAPI_KEY_CMD_SHOW_CURR_LOCN (<code>BRLAPI_KEY_CMD</code>(0) + 106)</h3>
<p>set speech location visibility on/off</p>
<h3>#define BRLAPI_KEY_CMD_SIXDOTS (<code>BRLAPI_KEY_CMD</code>(0) + 34)</h3>
<p>set text style 6-dot/8-dot</p>
<h3>#define BRLAPI_KEY_CMD_SKPBLNKWINS (<code>BRLAPI_KEY_CMD</code>(0) + 37)</h3>
<p>set skipping of blank windows on/off</p>
<h3>#define BRLAPI_KEY_CMD_SKPIDLNS (<code>BRLAPI_KEY_CMD</code>(0) + 36)</h3>
<p>set skipping of lines with identical content on/off</p>
<h3>#define BRLAPI_KEY_CMD_SLIDEWIN (<code>BRLAPI_KEY_CMD</code>(0) + 35)</h3>
<p>set sliding window on/off</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_CURR_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 89)</h3>
<p>speak current character</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_CURR_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 95)</h3>
<p>speak current line</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_CURR_LOCN (<code>BRLAPI_KEY_CMD</code>(0) + 105)</h3>
<p>speak speech location</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_CURR_WORD (<code>BRLAPI_KEY_CMD</code>(0) + 92)</h3>
<p>speak current word</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_FRST_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 98)</h3>
<p>go to and speak first non-blank character on line</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_FRST_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 100)</h3>
<p>go to and speak first non-blank line on screen</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_LAST_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 99)</h3>
<p>go to and speak last non-blank character on line</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_LAST_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 101)</h3>
<p>go to and speak last non-blank line on screen</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_NEXT_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 91)</h3>
<p>go to and speak next character</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_NEXT_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 97)</h3>
<p>go to and speak next line</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_NEXT_WORD (<code>BRLAPI_KEY_CMD</code>(0) + 94)</h3>
<p>go to and speak next word</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_PREV_CHAR (<code>BRLAPI_KEY_CMD</code>(0) + 90)</h3>
<p>go to and speak previous character</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_PREV_LINE (<code>BRLAPI_KEY_CMD</code>(0) + 96)</h3>
<p>go to and speak previous line</p>
<h3>#define BRLAPI_KEY_CMD_SPEAK_PREV_WORD (<code>BRLAPI_KEY_CMD</code>(0) + 93)</h3>
<p>go to and speak previous word</p>
<h3>#define BRLAPI_KEY_CMD_SPELL_CURR_WORD (<code>BRLAPI_KEY_CMD</code>(0) + 103)</h3>
<p>spell current word</p>
<h3>#define BRLAPI_KEY_CMD_SPKHOME (<code>BRLAPI_KEY_CMD</code>(0) + 62)</h3>
<p>go to current speech position</p>
<h3>#define BRLAPI_KEY_CMD_SWITCHVT <code>BRLAPI_KEY_CMD</code>(0X06)</h3>
<p>switch to virtual terminal</p>
<h3>#define BRLAPI_KEY_CMD_SWITCHVT_NEXT (<code>BRLAPI_KEY_CMD</code>(0) + 71)</h3>
<p>switch to next virtual terminal</p>
<h3>#define BRLAPI_KEY_CMD_SWITCHVT_PREV (<code>BRLAPI_KEY_CMD</code>(0) + 70)</h3>
<p>switch to previous virtual terminal</p>
<h3>#define BRLAPI_KEY_CMD_TIME (<code>BRLAPI_KEY_CMD</code>(0) + 81)</h3>
<p>show the current date and time</p>
<h3>#define BRLAPI_KEY_CMD_TOP (<code>BRLAPI_KEY_CMD</code>(0) + 9)</h3>
<p>go to top line</p>
<h3>#define BRLAPI_KEY_CMD_TOP_LEFT (<code>BRLAPI_KEY_CMD</code>(0) + 11)</h3>
<p>go to beginning of top line</p>
<h3>#define BRLAPI_KEY_CMD_TUNES (<code>BRLAPI_KEY_CMD</code>(0) + 46)</h3>
<p>set alert tunes on/off</p>
<h3>#define BRLAPI_KEY_CMD_UPPER (<code>BRLAPI_KEY_CMD</code>(0) + 78)</h3>
<p>set upper modifier of next typed character or emulated key on/off</p>
<h3>#define BRLAPI_KEY_CMD_WINDN (<code>BRLAPI_KEY_CMD</code>(0) + 4)</h3>
<p>go down several lines</p>
<h3>#define BRLAPI_KEY_CMD_WINUP (<code>BRLAPI_KEY_CMD</code>(0) + 3)</h3>
<p>go up several lines</p>
<h3>#define BRLAPI_KEY_CODE_MASK UINT64_C(0X000000001FFFFFFF)</h3>
<p>Mask for code of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_CODE_SHIFT 0</h3>
<p>Shift for code of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_FLAGS_MASK UINT64_C(0XFFFFFFFF00000000)</h3>
<p>Mask for flags of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_FLAGS_SHIFT 32</h3>
<p>Shift for flags of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_FLG(v) ((<code>brlapi_keyCode_t</code>)(v) &lt;&lt; <code>BRLAPI_KEY_FLAGS_SHIFT</code>)</h3>
<h3>#define BRLAPI_KEY_FLG_CONTROL <code>BRLAPI_KEY_FLG</code>(0X04)</h3>
<p>control key pressed</p>
<h3>#define BRLAPI_KEY_FLG_KBD_EMUL0 <code>BRLAPI_KEY_FLG</code>(0X0200)</h3>
<p>it is an emulation 0 scan code</p>
<h3>#define BRLAPI_KEY_FLG_KBD_EMUL1 <code>BRLAPI_KEY_FLG</code>(0X0400)</h3>
<p>it is an emulation 1 scan code</p>
<h3>#define BRLAPI_KEY_FLG_KBD_RELEASE <code>BRLAPI_KEY_FLG</code>(0X0100)</h3>
<p>it is a release scan code</p>
<h3>#define BRLAPI_KEY_FLG_LINE_SCALED <code>BRLAPI_KEY_FLG</code>(0X0100)</h3>
<p>scale arg=0X00-0XFF to screen height</p>
<h3>#define BRLAPI_KEY_FLG_LINE_TOLEFT <code>BRLAPI_KEY_FLG</code>(0X0200)</h3>
<p>go to beginning of line</p>
<h3>#define BRLAPI_KEY_FLG_META <code>BRLAPI_KEY_FLG</code>(0X08)</h3>
<p>meta key pressed</p>
<h3>#define BRLAPI_KEY_FLG_MOD1 <code>BRLAPI_KEY_FLG</code>(0x00000008)</h3>
<p>Standard X modifiers Mod1 modifier (AKA meta)</p>
<h3>#define BRLAPI_KEY_FLG_MOD2 <code>BRLAPI_KEY_FLG</code>(0x00000010)</h3>
<p>Mod2 modifier (usually numlock)</p>
<h3>#define BRLAPI_KEY_FLG_MOD3 <code>BRLAPI_KEY_FLG</code>(0x00000020)</h3>
<p>Mod3 modifier</p>
<h3>#define BRLAPI_KEY_FLG_MOD4 <code>BRLAPI_KEY_FLG</code>(0x00000040)</h3>
<p>Mod4 modifier</p>
<h3>#define BRLAPI_KEY_FLG_MOD5 <code>BRLAPI_KEY_FLG</code>(0x00000080)</h3>
<p>Mod5 modifier (usually Alt-Gr)</p>
<h3>#define BRLAPI_KEY_FLG_MOTION_ROUTE <code>BRLAPI_KEY_FLG</code>(0X0400)</h3>
<p>bring cursor into window after function</p>
<h3>#define BRLAPI_KEY_FLG_REPEAT_DELAY <code>BRLAPI_KEY_FLG</code>(0X4000)</h3>
<p>wait before repeating</p>
<h3>#define BRLAPI_KEY_FLG_REPEAT_INITIAL <code>BRLAPI_KEY_FLG</code>(0X8000)</h3>
<p>execute command on key press</p>
<h3>#define BRLAPI_KEY_FLG_REPEAT_MASK (<code>BRLAPI_KEY_FLG_REPEAT_INITIAL</code> | <code>BRLAPI_KEY_FLG_REPEAT_DELAY</code>)</h3>
<p>mask for all repeat flags</p>
<h3>#define BRLAPI_KEY_FLG_SHIFT <code>BRLAPI_KEY_FLG</code>(0X01)</h3>
<p>shift key pressed</p>
<h3>#define BRLAPI_KEY_FLG_TOGGLE_MASK (<code>BRLAPI_KEY_FLG_TOGGLE_ON</code> | <code>BRLAPI_KEY_FLG_TOGGLE_OFF</code>)</h3>
<p>mask for all toggle flags</p>
<h3>#define BRLAPI_KEY_FLG_TOGGLE_OFF <code>BRLAPI_KEY_FLG</code>(0X0200)</h3>
<p>disable feature</p>
<h3>#define BRLAPI_KEY_FLG_TOGGLE_ON <code>BRLAPI_KEY_FLG</code>(0X0100)</h3>
<p>enable feature</p>
<h3>#define BRLAPI_KEY_FLG_UPPER <code>BRLAPI_KEY_FLG</code>(0X02)</h3>
<p>convert to uppercase</p>
<h3>#define BRLAPI_KEY_MAX UINT64_C(0XFFFFFFFFFFFFFFFF)</h3>
<p>Brlapi_keyCode_t&#8217;s biggest value </p>
<p> As defined in &lt;stdint.h&gt;</p>
<h3>#define BRLAPI_KEY_SYM_BACKSPACE UINT64_C(0X0000FF08)</h3>
<p>Standard X keysyms</p>
<h3>#define BRLAPI_KEY_SYM_DELETE UINT64_C(0X0000FFFF)</h3>
<h3>#define BRLAPI_KEY_SYM_DOWN UINT64_C(0X0000FF54)</h3>
<h3>#define BRLAPI_KEY_SYM_END UINT64_C(0X0000FF57)</h3>
<h3>#define BRLAPI_KEY_SYM_ESCAPE UINT64_C(0X0000FF1B)</h3>
<h3>#define BRLAPI_KEY_SYM_FUNCTION UINT64_C(0X0000FFBE)</h3>
<h3>#define BRLAPI_KEY_SYM_HOME UINT64_C(0X0000FF50)</h3>
<h3>#define BRLAPI_KEY_SYM_INSERT UINT64_C(0X0000FF63)</h3>
<h3>#define BRLAPI_KEY_SYM_LEFT UINT64_C(0X0000FF51)</h3>
<h3>#define BRLAPI_KEY_SYM_LINEFEED UINT64_C(0X0000FF0D)</h3>
<h3>#define BRLAPI_KEY_SYM_PAGE_DOWN UINT64_C(0X0000FF56)</h3>
<h3>#define BRLAPI_KEY_SYM_PAGE_UP UINT64_C(0X0000FF55)</h3>
<h3>#define BRLAPI_KEY_SYM_RIGHT UINT64_C(0X0000FF53)</h3>
<h3>#define BRLAPI_KEY_SYM_TAB UINT64_C(0X0000FF09)</h3>
<h3>#define BRLAPI_KEY_SYM_UNICODE UINT64_C(0X01000000)</h3>
<h3>#define BRLAPI_KEY_SYM_UP UINT64_C(0X0000FF52)</h3>
<h3>#define BRLAPI_KEY_TYPE_CMD UINT64_C(0X0000000020000000)</h3>
<p>Braille command brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_TYPE_MASK UINT64_C(0X00000000E0000000)</h3>
<p>Mask for type of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_TYPE_SHIFT 29</h3>
<p>Shift for type of brlapi_keyCode_t</p>
<h3>#define BRLAPI_KEY_TYPE_SYM UINT64_C(0X0000000000000000)</h3>
<p>X Keysym brlapi_keyCode_t</p>
<h3>#define BRLAPI_PRIuKEYCODE PRIu64</h3>
<p>Unsigned print format for brlapi_keyCode_t</p>
<h3>#define BRLAPI_PRIxKEYCODE PRIx64</h3>
<p>Hex print format for brlapi_keyCode_t</p>
<h2>Typedef Documentation</h2>
<h3>typedef uint64_t <code>brlapi_keyCode_t</code></h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
