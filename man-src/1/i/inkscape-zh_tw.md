---
title: "inkscape-zh_tw(1)"
name: "inkscape-zh_tw"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape-zh_tw/"
---

<h2>名稱</h2>
<p>Inkscape &#8211; <font SIZE="-1">SVG </font>(Scalable Vector Graphics) 編輯程式。</p>
<h2>概要</h2>
<p><tt>&quot;inkscape [選項] [檔名 ...]&quot;</tt> </p>
<p> 選項: </p>
<pre> -?, --help 
 --usage 
 -V, --version
 -f, --file=檔名 
 -e, --export-png=檔名 
 -a, --export-area=x0:y0:x1:y1 
 -C, --export-area-page
 -D, --export-area-drawing
 --export-area-snap
 -i, --export-id=ID 
 -j, --export-id-only 
 -t, --export-use-hints
 -b, --export-background=顏色 
 -y, --export-background-opacity=數值 
 -d, --export-dpi=DPI 
 -w, --export-width=寬度 
 -h, --export-height=高度 
 -P, --export-ps=FILENAME
 -E, --export-eps=FILENAME
 -A, --export-pdf=FILENAME
 --export-pdf-version=VERSION-STRING
 --export-latex
 --export-ps-level {2,3}
 -T, --export-text-to-path
 --export-ignore-filters
 -l, --export-plain-svg=檔名 
 -p, --print=印表機
 -I, --query-id=ID 
 -X, --query-x
 -Y, --query-y
 -W, --query-width
 -H, --query-height
 -S, --query-all
 -x, --extension-directory
 --verb-list
 --verb=動詞-ID
 --select=物件-ID
 --shell
 -g, --with-gui 
 -z, --without-gui 
 --vacuum-defs
 --g-fatal-warnings</pre>
<h2>描述</h2>
<p><code>Inkscape</code> 是一款<code>可縮放式向量圖形 (</code><font SIZE="-1"><code>SVG</code></font><code>)</code> 格式繪圖檔的圖形介面編輯程式，類似 <code>Adobe Illustrator</code>、 <code>CorelDraw</code>、<code>Xara Xtreme</code> 等。Inkscape 的特點包括多功能形狀、貝茲曲線、手繪、多行文字、文字置 於路徑、透明混合處理、任意變形、漸層和圖樣填充節點編輯、支援多種匯出和匯入格式包含 <font SIZE="-1">PNG</font> 和 PDF、群組、圖 層、即時仿製和其他許許多多的功能。使用介面讓設計者使用起來舒適且效率高，由於保持與 <font SIZE="-1"><code>GNOME</code></font> 標準相容， 因此熟悉其他 <font SIZE="-1">GNOME</font> 應用程式的使用者能迅速地學習並掌握程式的使用介面。 </p>
<p> <font SIZE="-1"><code>SVG</code></font> 是 W3C 針對 2D 向量繪圖制定的標準 <font SIZE="-1">XML</font> 格式。 <font SIZE="-1">SVG</font> 可於圖畫中使用點、路徑和基本形狀來定義物件。 顏色、字型、邊框寬度&#8230;等等可作為「樣式」屬性指定給這些物件。由於 <font SIZE="-1">SVG</font> 的目標是成為標準格式，也因為 <font SIZE="-1">SVG</font> 檔為純文字檔/xml，所以有相當多的程式可能使用 <font SIZE="-1">SVG</font> 檔並有多種用途。 </p>
<p> <code>Inkscape</code> 使用 <font SIZE="-1">SVG</font> 作為內定文件格式，並且以成為在開放原碼社群中完整相容 <font SIZE="-1">SVG</font> 格式的繪圖程式為目標。</p>
<h2>選項</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>顯示說明訊息</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>顯示 Inkscape 版本和建立日期。</p>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></p>
<dd>匯出 <font SIZE="-1">PNG</font> 時，以 <font SIZE="-1">SVG</font> 使用者單位設定匯出範圍 (在 Inkscape <font SIZE="-1">SVG</font> 中一般用匿名長度單位)。 預設是匯出整個文件畫布。原點 (0,0) 為左下角。</p>
<dt><code>-C</code>, <code>&#8211;export-area-page</code></p>
<dd>匯出 PNG、PDF、PS 和 <font SIZE="-1">EPS</font> 時，匯出範圍是畫布 (頁面)。這是匯出 PNG、PDF 和 <font SIZE="-1">PS</font> 的預設值，所以你不必指 定這個，除非你使用 &#8211;export-id 來匯出指定的物件。匯出 <font SIZE="-1">EPS</font> 時，這就不是預設值；此外，對於 EPS，格式的 規格不允許外框邊界超出內容範圍。這表示當 &#8211;export-area-canvas 用於 <font SIZE="-1">EPS</font> 匯出時，如果內容的外框邊界較 小則畫布的外框邊界會被向內裁剪成內容的外框邊界。</p>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></p>
<dd>匯出 PNG、PDF、PS 和 <font SIZE="-1">EPS</font> 時，匯出範圍為繪畫部份 (不是畫布)，即文件全部物件的外框邊界 (如果使用 &#8211;export -id 則是匯出物件的外框邊界)。 使用這個選項，匯出的圖片會顯示文件中所有的可見物件，而不會有頁邊空白或裁剪。 這是 <font SIZE="-1">EPS</font> 預設的匯出範圍。對於 PNG，這個可以和 &#8211;export-use-hints 結合使用。</p>
<dt><code>&#8211;export-area-snap</code></p>
<dd>匯出 <font SIZE="-1">PNG</font> 時，向外捉取匯出範圍為最接近的整數 <font SIZE="-1">SVG</font> 使用者單位 (px) 數值。如果你使用預設的匯出解析度 90 dpi 且你的圖形是像素捉取來最小化平滑，這項改變允許你維持這種校正方式，即使你正要匯出的物件的外框邊界 (使用 &#8211;export-id 或 &#8211;export-area-drawing) 是本身而不是像素校正。</p>
<dt><code>-b</code> <i>顏色</i>, <code>&#8211;export-background</code>=<i>顏色</i></p>
<dd>匯出 <font SIZE="-1">PNG</font> 的背景顏色。 可以是任何 <font SIZE="-1">SVG</font> 的顏色字串，例如 &#8220;#ff007f&#8221; 或 &#8220;rgb(255, 0, 128)&#8221;。 如果沒有設定顏色，那麼就會使用在 Inkscape 文件選項對話窗所設定的頁面顏色 (儲存在 pagecolor= sodipodi:namedview 的屬性)。</p>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>DPI</i></font><i></i>, <code>&#8211;export-dpi</code>=<i></i><font SIZE="-1"><i>DPI</i></font><i></i></p>
<dd>匯出 <font SIZE="-1">PNG</font> 所使用的解析度。 當匯出為 PS、EPS 或 <font SIZE="-1">PDF </font>(除非你指定 &#8211;export-ignore-filters 禁止點陣化) 時，也用於退回套用濾鏡 物件的點陣化過程。預設值為 90 dpi，其對應成 1 <font SIZE="-1">SVG</font> 使用者單位 (px, 亦稱「使用者單位」) 匯出為 1 點 陣圖像素。 如果和 &#8211;export-use-hints 一起使用，這個數值會覆蓋 <font SIZE="-1">DPI</font> 內定值。</p>
<dt><code>-e</code> <i>檔名</i>, <code>&#8211;export-png</code>=<i>檔名</i></p>
<dd>指定匯出 <font SIZE="-1">PNG</font> 的檔名。 如果指定的檔名已經存在，則不會詢問便覆蓋原有的檔案。</p>
<dt><code>-f</code> <i>檔名</i>, <code>&#8211;file</code>=<i>檔名</i></p>
<dd>開啟指定的文件。 選項字串可以省略，即你可以不要輸入 -f 只列出檔名。</p>
<dt><code>-g</code>, <code>&#8211;with-gui</code></p>
<dd>試著使用圖形介面 (在 Unix 系統，即使沒有設定 <tt>$DISPLAY</tt> 也會使用 X server)。</p>
<dt><code>-h</code> <i>高度</i>, <code>&#8211;export-height</code>=<i>高度</i></p>
<dd>匯出點陣圖的高度，單位為像素。 這個數值會覆蓋 &#8211;export-dpi 設定值 (如果和 &#8211;export-use-hints 同時使用，會覆蓋 <font SIZE="-1">DPI</font> 內定值)。</p>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i>, <code>&#8211;export-id</code>=<i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>For <font SIZE="-1">PNG, PS, EPS, PDF</font> and plain <font SIZE="-1">SVG</font> export, the id attribute value of the object that you want to export from the document; all other objects are not exported. By default the exported area is the bounding box of the object; you can override this using &#8211;export-area (<font SIZE="-1">PNG</font> only) or &#8211;export-area-page.</p>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></p>
<dd>For <font SIZE="-1">PNG</font> and plain <font SIZE="-1">SVG,</font> only export the object whose id is given in &#8211;export-id. All other objects are hidden and won&#8217;t show in export even if they overlay the exported object. Without &#8211;export-id, this option is ignored. For <font SIZE="-1">PDF</font> export, this is the default, so this option has no effect.</p>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code>=<i>檔名</i></p>
<dd>匯出文件為普通的 <font SIZE="-1">SVG</font> 格式，沒有 sodipodi: 或 inkscape: 名稱集也沒有 <font SIZE="-1">RDF</font> 後設資料。</p>
<dt><code>-x</code>, <code>&#8211;extension-directory</code></p>
<dd>列出 Inkscape 目前設定為使用且存在的擴充模組目錄。這選項用於外部擴充模組使用相同設定作為原始的 Inkscape 安裝。</p>
<dt><code>&#8211;verb-list</code></p>
<dd>依照 <font SIZE="-1">ID</font> 列出在 Inkscape 中全部可用的動詞。這 <font SIZE="-1">ID</font> 可用在定義按鍵對應或選單中。也可以和 &#8211;verb 命令 列選項一起使用。</p>
<dt><code>&#8211;verb</code>=<i>動詞-ID</i>, <code>&#8211;select</code>=<i>物件-ID</i></p>
<dd>這兩個選項一起使用可由命令列上提供一些 Inkscape 的基本腳本。於命令列上要執行多少次都可以，而且可在每一 個指定的文件上執行。 </p>
<p> 其 &#8211;verb 指令會執行某個指定的動詞，就像從選單或按鈕上呼叫一樣。如果執行的是部份動詞便會跳出對話窗。 使用 &#8211;verb-list 命令列選項可取得可用動詞 <font SIZE="-1">ID</font> 的清單。 </p>
<p> 而 &#8211;select 指令會選取被指定 <font SIZE="-1">ID</font> 的物件。此選項允許對選取物件執行各種動詞。使用 &#8211;verb=EditDeselect 可移除所有選取的項目。可用的物件 <font SIZE="-1">ID</font> 取決於文件指定載入哪些物件。</p>
<dt><code>-p</code> <i>印表機</i>, <code>&#8211;print</code>=<i>印表機</i></p>
<dd>用指定的印表機來列印文件，使用 `lpr -P <font SIZE="-1">PRINTER</font>&#8216; 來指定印表機。 用 `| 指令&#8217; 來指定一個不同的指令到管線中，或用 `&gt; 檔名&#8217; 來寫入 PostScript 輸出到檔案而不是印表機。 記得加上適當的引號，例如 </p>
<p> inkscape &#8211;print=&#8217;| ps2pdf &#8211; 我的文件.pdf&#8217; 我的文件.svg</p>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></p>
<dd>使用匯出檔名和儲存在匯出物件中的 <font SIZE="-1">DPI</font> 內定值 (只能和 &#8211;export-id 一起使用)。 當你從 Inkscape 內部匯出選取範圍時會自動設定為這些內定值。 例如，你用 Inkscape 圖形介面從 document.svg 裡將 id=&#8220;path231&#8221; 的形狀以 300 dpi 匯出成 /home/me/shape.png ，並儲存文件，之後你便可簡單地用下面的指令以相同的解析度重新匯出相同的檔案 </p>
<p> inkscape -i path231 -t 文件.svg </p>
<p> 如果你將這個選項和 &#8211;export-dpi、&#8211;export-width 或 &#8211;export-height 一起使用,那麼 <font SIZE="-1">DPI</font> 內定值會被忽略並使用命令列上的數值。 如果你將這個選項和 &#8211;export-png 一起使用，那麼檔名內定值會被忽略並使用命令列上的檔名。</p>
<dt><code>-w</code> <i>寬度</i>, <code>&#8211;export-width</code>=<i>寬度</i></p>
<dd>匯出點陣圖的寬度，單位為像素。 這個數值會覆蓋 &#8211;export-dpi 設定值 (如果和 &#8211;export-use-hints 同時使用則會覆蓋 <font SIZE="-1">DPI</font> 內定值)。</p>
<dt><code>-y</code> <i>數值</i>, <code>&#8211;export-background-opacity</code>=<i>數值</i></p>
<dd>匯出 <font SIZE="-1">PNG</font> 背景的不透明度。 這個數值可以是 0.0 到 1.0 之間的數值 (0.0 表示完全透明，1.0 表示完全不透明) 或者大於 1 到 255 以內的數值 (255 代表完全不透明)。 如果沒有設定數值且沒有使用 -b 選項，那麼就會使用在 Inkscape 文件選項對話窗所設定的頁面不透明度 (儲存 在 inkscape:pageopacity= sodipodi:namedview 的屬性)。 如果沒有設定數值但有使用 -b 選項，那麼會使用 255 (完全不透明)。</p>
<dt><code>-P</code> <i>檔名</i>, <code>&#8211;export-ps</code>=<i>檔名</i></p>
<dd>將文件匯出成 PostScript 格式。注意 PostScript 不支援透明，所以原本 <font SIZE="-1">SVG</font> 中的透明物件都會自動轉成點 陣圖。使用的字型成子集合並嵌入。預設的匯出範圍是畫布；你可以用 &#8211;export-area-drawing 將匯出範圍設定 成繪圖部份。你可指定 &#8211;export-id 來匯出單一物件 (其餘全部隱藏); 假如那樣的話匯出範圍就是物件的外框邊 界，但可用 &#8211;export-area-canvas 設定成畫布。</p>
<dt><code>-E</code> <i>檔名</i>, <code>&#8211;export-eps</code>=<i>檔名</i></p>
<dd>將文件匯出成封裝的 PostScript 格式。注意 PostScript 不支援透明，所以原始 <font SIZE="-1">SVG</font> 中的透明物件都會自動轉成點 陣圖。使用的字型成子集合並嵌入。預設的匯出範圍是繪圖部份；你可設定成畫布，不過會看見 &#8211;export-area-canvas 的適用限制。你可以指定 &#8211;export-id 來匯出單一物件 (其餘全部隱藏)。</p>
<dt><code>-A</code> <i>檔名</i>, <code>&#8211;export-pdf</code>=<i>檔名</i></p>
<dd>將文件匯出成 <font SIZE="-1">PDF</font> 格式。這種格式會保存原始 <font SIZE="-1">SVG</font> 中的透明度。使用的字型成子集合並嵌入。 預設的匯出範圍是畫 布；你可以用 &#8211;export-area-drawing 將匯出範圍設定成繪圖部份。你可以指定 &#8211;export-id 來匯出單一物 件 (其餘全部隱藏); 假如那樣的話匯出範圍就是物件的外框邊界，但可用 &#8211;export-area-canvas 設定成畫布。</p>
<dt><code>&#8211;export-pdf-version</code>=<i>PDF-VERSION</i></p>
<dd>Select the <font SIZE="-1">PDF</font> version of the exported <font SIZE="-1">PDF</font> file. This option basically exposes the <font SIZE="-1">PDF</font> version selector found in the PDF-export dialog of the <font SIZE="-1">GUI.</font> You must provide one of the versions from that combo-box, e.g. &#8220;1.4&#8221;. The default pdf export version is &#8220;1.4&#8221;.</p>
<dt><code>&#8211;export-latex</code></p>
<dd>(PS、EPS 和 <font SIZE="-1">PDF</font> 匯出) 用來建立 LaTeX 文件的圖片，而圖片的文字則由 LaTeX 排版。當匯出成 <font SIZE="-1">PDF/PS/EPS</font> 格式時，此選項會將輸出分離成一個 <font SIZE="-1">PDF/PS/EPS</font> 檔 (例如用 &#8211;export-pdf 指定) 和 LaTeX 檔。文字不會輸出到 <font SIZE="-1">PDF/PS/EPS</font> 檔案裡，但會出現在 LaTeX 檔案。這個 LaTeX 檔案包含 PDF/PS/EPS。輸入 (\input{image.tex}) LaTeX 檔案到你的 LaTeX 文件會顯示圖片和全部由 LaTeX 排版的文字。查閱結果的 LaTeX 檔案可得知更多資訊。也請查看 GNUPlot 的「epslatex」輸出終端機。</p>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></p>
<dd>Convert text objects to paths on export, where applicable (for <font SIZE="-1">PS, EPS, PDF</font> and <font SIZE="-1">SVG</font> export).</p>
<dt><code>&#8211;export-ignore-filters</code></p>
<dd>將套用濾鏡的物件 (例如這些物件套用模糊) 匯出成向量屬性，忽略濾鏡 (匯出 PS、EPS 和PDF 時)。 在預設情況下，全部套用濾鏡的物件會以 &#8211;export-dpi (預設為 90 dpi) 的解析度轉成點陣圖以維持外觀。</p>
<dt><code>-I</code>, <code>&#8211;query-id</code></p>
<dd>設定要查詢尺寸的物件 ID。如果沒有設定，查詢選項會回傳繪圖部份的尺寸 (即文件的全部物件)，而不是頁面或 檢視外框。</p>
<dt><code>-X</code>, <code>&#8211;query-x</code></p>
<dd>查詢繪圖部份的 X 坐標或用 &#8211;query-id 所指定物件的 X 坐標。回傳值的單位是 px (<font SIZE="-1">SVG</font> 使用者單位)。</p>
<dt><code>-Y</code>, <code>&#8211;query-y</code></p>
<dd>查詢繪圖部份的 Y 坐標或用 &#8211;query-id 所指定物件的 Y 坐標。回傳值的單位是 px (<font SIZE="-1">SVG</font> 使用者單位)。</p>
<dt><code>-W</code>, <code>&#8211;query-width</code></p>
<dd>查詢繪圖部份的寬度或用 &#8211;query-id 所指定物件的寬度。回傳值的單位是 px (<font SIZE="-1">SVG</font> 使用者單位)。</p>
<dt><code>-H</code>, <code>&#8211;query-height</code></p>
<dd>查詢繪圖部份的高度或用 &#8211;query-id 所指定物件的高度。回傳值的單位是 px (<font SIZE="-1">SVG</font> 使用者單位)。</p>
<dt><code>-S</code>, <code>&#8211;query-all</code></p>
<dd>列印一份 <font SIZE="-1">SVG</font> 文件中已定義 <font SIZE="-1">ID</font> 的所有物件以逗點區隔的清單，與 x、y、寬度和高度數值同樣。</p>
<dt><code>&#8211;shell</code></p>
<dd>使用這個參數，Inkscape 會進入互動式命令列 shell 模式。在這種模式中，你在提示符上輸入指令然後 Inkscape 執行，而不必對每一道指令執行新的 Inkscape。這個功能對腳本和伺服器用途極為有用：它沒有加入任何新功能，但可 讓任何多次呼叫 Inkscape 執行命令列任務 (比如匯出或轉換) 腳本的速度更快、需要更少的記憶體。 在 shell 模式中的每一道指令必須是完全正確的 Inkscape 命令列但不含 Inkscape 程式名稱， 例如 &#8220;檔案.svg &#8211;export-pdf=檔案.pdf&#8221;。</p>
<dt><code>&#8211;vacuum-defs</code></p>
<dd>從 <font SIZE="-1">SVG</font> 檔案的 &lt;lt&gt;defs&lt;gt&gt; 段落中移除所有未使用的項目。如果這個選項與 &#8211;export-plain-svg 一起調用， 只有匯出的檔案會有作用。如果單獨使用會適當地修飾所指定的檔案。</p>
<dt><code>-z</code>, <code>&#8211;without-gui</code></p>
<dd>不要開啟圖形介面 (在 Unix 系統，不使用 X server)；只從終端機處理檔案。 這被假定為 -p、-e、-l 和 &#8211;vacuum-defs 選項。</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd>這標準 <font SIZE="-1">GTK</font> 選項會強制出現任何警告時，使 Inkscape 中止 (對除錯很有用)。</p>
<dt><code>&#8211;usage</code></p>
<dd>顯示簡單的使用訊息。</dl>
<h2>組態設定</h2>
<p>主要的組態設定檔放在 ~/.config/Inkscape/preferences.xml； 組態設定檔儲存各種設定值，可在 Inkscape 中變更 (大部份在 Inkscape 偏好設定對話窗)。也可以在那裡的子目錄中放置你自己的組態設定檔： </p>
<p> $HOME/.config/Inkscape/extensions/ &#8211; 擴充模組。 </p>
<p> $HOME/.config/Inkscape/icons/ &#8211; 圖示。 </p>
<p> $HOME/.config/Inkscape/keys/ &#8211; 鍵盤對應。 </p>
<p> $HOME/.config/Inkscape/templates/ &#8211; 新增檔案的範本。</p>
<h2>診斷</h2>
<p>程式執行成功時會回傳零或者執行失敗時回傳不為零的值。 </p>
<p> 各種錯誤訊息和警告可列印到 <font SIZE="-1">STDERR</font> 或 STDOUT。如果程式怪異地產生一個特殊的 <font SIZE="-1">SVG</font> 檔案或不正常關閉，它是 查看這次輸出的有用線索。</p>
<h2>範例</h2>
<p>雖然 <code>Inkscape</code> 很明顯地主要是作為一款圖形介面的應用程式，但同樣能在命令列上處理 SVG。 </p>
<p> 用圖形介面開啟一個 <font SIZE="-1">SVG</font> 檔案： </p>
<pre> inkscape 檔名.svg</pre>
<p>從命令列上列印一個 <font SIZE="-1">SVG</font> 檔案： </p>
<pre> inkscape 檔名.svg -p '| lpr'</pre>
<p>將一個 <font SIZE="-1">SVG</font> 檔以預設的解析度 90dpi 匯出成 <font SIZE="-1">PNG </font>(1 <font SIZE="-1">SVG</font> 使用者單位轉變成 1 點陣圖像素)： </p>
<pre> inkscape 檔名.svg --export-png=檔名.png</pre>
<p>相同，但強制 <font SIZE="-1">PNG</font> 檔案為 600&#215;400 像素： </p>
<pre> inkscape 檔名.svg --export-png=檔名.png -w600 -h400</pre>
<p>相同，但匯出繪圖部份 (全部物件的外框邊界)，不是頁面： </p>
<pre> inkscape 檔名.svg --export-png=檔名.png --export-area-drawing</pre>
<p>將 id=&#8220;text1555&#8221; 物件匯出成 PNG，當從圖形介面匯出時，使用輸出檔名和上次使用的解析度： </p>
<pre> inkscape 檔名.svg --export-id=text1555 --export-use-hints</pre>
<p>相同，但使用預設 90 dpi 解析度，指定檔名，並且向外捉取匯出範圍為最接近整個 <font SIZE="-1">SVG</font> 使用者單位的值 (維持物件的像素校正，因此最小平滑化)： </p>
<pre> inkscape 檔名.svg --export-id=text1555 --export-png=文字.png --export-snap-area</pre>
<p>將一個 Inkscape <font SIZE="-1">SVG</font> 文件轉換成普通的 SVG： </p>
<pre> inkscape 檔名1.svg --export-plain-svg=檔名2.svg</pre>
<p>將 <font SIZE="-1">SVG</font> 文件轉成 EPS，全部的文字轉換成路徑： </p>
<pre> inkscape 檔名.svg --export-eps=檔名.eps --export-text-to-path</pre>
<p>查詢 id=&#8220;text1555&#8221; 物件的寬度： </p>
<pre> inkscape 檔名.svg --query-width --query-id text1555</pre>
<p>再製 id=&#8220;path1555&#8221; 的物件，將再製物件旋轉 90 度，儲存 <font SIZE="-1">SVG</font> 並離開： </p>
<pre> inkscape 檔名.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose</pre>
<h2>環境</h2>
<p><font SIZE="-1"><code>DISPLAY</code></font> 可取得預設主機和顯示編號。 </p>
<p> <font SIZE="-1"><code>TMPDIR</code></font> 可設定暫存檔使用的預設目錄的路徑。目錄必須存在。 </p>
<p> <font SIZE="-1"><code>INKSCAPE_PROFILE_DIR</code></font> to set the path of the directory to use for the user profile.</p>
<h2>主題</h2>
<p>可從目錄 $HOME/.inkscape/icons/ 載入不同的圖示組來替代預設的$PREFIX/share/inkscape/icons/icons.svg 檔案。 圖示按照名稱載入 (例如 <i>fill_none.svg</i>)，如果沒有找到符合名稱的圖示，那麼就會從 <i>icons.svg</i> 載入。 如果圖示不從這些位置載入，就會退回使用預設的系統位置。 </p>
<p> 藉由 <font SIZE="-1">SVG ID</font> 和比對圖示名稱從 <font SIZE="-1">SVG</font> 檔中搜尋並載入需要的圖示。(例如，要從一個檔案載入 &#8220;fill_none&#8221; 圖示， 外框邊界會尋找 <font SIZE="-1">SVG ID </font>&#8220;fill_none&#8221; 將其作為圖示，不管是來自 <i>fill_none.svg</i> 或 <i>icons.svg</i>。)</p>
<h2>其他資訊</h2>
<p>搜尋 <code>Inkscape</code> 資訊的最佳地點是在 <a rel="nofollow" href="http://www.inkscape.org/。">http://www.inkscape.org/。</a> 網站上有新聞、說明文件、教學、範例、郵件論壇存檔、最新發佈的程式版本、程式錯誤和功能需求資料庫、論壇&#8230;等等。</p>
<h2>參見</h2>
<p>potrace, cairo, <i><a href="/docs/linux/man/1-rsvg/">rsvg</a></i>(1), batik, ghostscript, pstoedit. </p>
<p> <font SIZE="-1">SVG</font> 相容測試工具: <a rel="nofollow" href="http://www.w3.org/Graphics/SVG/Test/">http://www.w3.org/Graphics/SVG/Test/</a> </p>
<p> <font SIZE="-1">SVG</font> 驗證工具: <a rel="nofollow" href="http://jiggles.w3.org/svgvalidator/">http://jiggles.w3.org/svgvalidator/</a> </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.1 Specification</i> <i>W3C Recommendation 14 January 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.2 Specification</i> <i>W3C Working Draft 13 November 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG12/">http://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i></i><font SIZE="-1"><i>SVG 1.1/1.2/2.0</i></font><i> Requirements</i> <i>W3C Working Draft 22 April 2002</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG2Reqs/">http://www.w3.org/TR/SVG2Reqs/</a>&gt; </p>
<p> <i>Document Object Model (</i><font SIZE="-1"><i>DOM</i></font><i>): Level 2 Core</i> <i>Arnaud Le Hors et al editors, W3C</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/DOM-Level-2-Core/">http://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>Gui 重點</h2>
<p>閱讀在 說明 &gt; 指導手冊 中的教學來學習 Inkscape 圖形介面的操作。 </p>
<p> 除了 <font SIZE="-1">SVG</font> 外，Inkscape 可以匯入 (檔案 &gt; 匯入) 多數的點陣圖格式 (PNG、BMP、JPG、XPM、GIF 等)、 普通純文字檔 (需要 Perl)、PS 和 <font SIZE="-1">EPS </font>(需要 Ghostscript)、PDF 和 <font SIZE="-1">AI</font> 格式 (<font SIZE="-1">AI</font> 版本 9.0 或更新)。 </p>
<p> Inkscape exports 32-bit <font SIZE="-1">PNG</font> images (File &gt; Export <font SIZE="-1">PNG</font> Image) as well as <font SIZE="-1">AI, PS, EPS, PDF, DXF,</font> and several other formats via File &gt; Save as. </p>
<p> Inkscape 能用繪圖板畫筆的壓力及傾斜感應來變化寬度、角度和一些工具的作用力，包括美工筆。 </p>
<p> Inkscape 包含一個嵌入的 Potrace 點陣圖描繪引擎 (<a rel="nofollow" href="http://potrace.sf.net)">http://potrace.sf.net)</a> 圖形介面前端。 </p>
<p> Inkscape 能使用外部腳本 (stdin-to-stdout 過濾器)，腳本會以擴充功能選單上的命令方式呈現。腳本可以 有設定各種參數的圖形介面對話窗，而且能透過命令列取得所選物件的 ID。Inkscape 提供各式各樣用 Python 寫成的特效模組。</p>
<h2>按鍵對應</h2>
<p>查看 doc/keys.html 以取得鍵盤和滑鼠快捷鍵的完整清單，或在說明選單中使用按鍵和滑鼠指令。</p>
<h2>程式錯誤</h2>
<p>已經知道許多程式錯誤；請到網站 (inkscape.org) 檢閱已回報的錯誤並回報新發現的問題。也請看看你使用版 本的發佈說明中已知問題段落內容 (檔案「NEWS」)。</p>
<h2>作者</h2>
<p>這個程式碼庫的存在要歸功於各個時期的許多貢獻者。下列的名單當然不完整，但用來正式向齊心致力於這個程式的 許多人致謝： </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Robert Crosbie, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Danilo Šegan, Abhishek Sharma, Shivaken, Michael Sloan, John Smith, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, David Yip, Masatake Yamato </p>
<p> This man page was put together by Bryce Harrington &lt;brycehar [at] bryceharrington.org&gt;.</p>
<h2>歷史</h2>
<p>後來變成 Inkscape 的程式碼庫始於 1999 年的程式 Gill (由 Raph Levien 建立的 <font SIZE="-1">GNOME</font> 繪圖程式)。 Gill 的最終目標是支援全部的 SVG。Raph 實現了 PostScript 貝茲曲線成像模型，包括邊框和填充、線段 端點樣式、線段接合樣式、文字&#8230;等等。Raph 的 Gill 網頁位於 <a rel="nofollow" href="http://www.levien.com/svg/。Gill">http://www.levien.com/svg/。Gill</a> 的開發工作在 2000 年時似乎已經變慢或停止。 </p>
<p> 接下來這個程式碼庫化身為極受歡迎的程式 Sodipodi，由 Lauris Kaplinski 主導。經過數年的發展，這個 程式碼庫已轉變為一個強大的繪圖程式，加入了一些新特性，支援多語言，移植到 Windows 和其他操作系統，並 淘汰某些相依套件。 </p>
<p> 於 2003 年時由四名活躍的 Sodipodi 開發人員 － Bryce Harrington、MenTaLguY、Nathan Hurst 和 Ted Gould 成立 Inkscape 計劃，想要以專注於 <font SIZE="-1">SVG</font> 相容、介面外觀風格和開放開發機會吸引更多參與 者的觀點為程式碼庫帶來新的方向。此計劃進展迅速，獲得許多非常活躍的貢獻和功能。 </p>
<p> 計劃早期的許多工作專注於程式碼的穩定和國際化。從 Sodipodi 繼承的原始圖形輸出引擎摻入許多數學角，因而 導致當程式超出正常使用範圍時會意外地不正常關閉；用 Livarot 取代原本的圖形輸出引擎，雖然不夠完美，但 程式錯誤明顯地減少。此計劃也有經常收養提交的程式碼的做法，並鼓勵使用者去試用程式的開發版本快照；這有助 於迅速發現新的程式錯誤，並且保證使用者能輕易地校驗修復狀況。因此，Inkscape 發佈的版本已經普遍贏得了穩健可靠的聲譽。 </p>
<p> 同樣的，努力走向國際化及介面本地化，這有助於此程式獲得世界各地的幫助與貢獻。 </p>
<p> 大致上來說，Inkscape 已經在開放原碼的視覺魅力上產生正面的影響，作為用來製作和分享圖示、啟動畫面、網站 設計等的工具。從某一點來看，「這只是一個繪圖程式」，但 Inkscape 已經扮演一個重要的角色，使開放原始碼 帶給廣大愛好者更多的視覺饗宴。</p>
<h2>著作權和許可證</h2>
<p><code>著作權 (C)</code> 1999-2008 作者所有。 </p>
<p> <code>Inkscape</code> 是自由軟體；你可以在遵守 <font SIZE="-1">GPL</font> 許可證情形下重新發佈或修改它。</p>
