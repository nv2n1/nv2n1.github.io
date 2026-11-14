---
title: "ghc(1)"
name: "ghc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ghc/"
description: "GHC – the Glasgow Haskell Compiler"
---

<h2>NAME</h2>
<p> GHC &#8211; the Glasgow Haskell Compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>ghc</code> [<i>option</i>|<i>filename</i>]&#8230;<br />
 <code>ghci</code> [<i>option</i>|<i>filename</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ghc</code> and <code>ghci</code> commands. Note that <code>ghci</code> is not yet available on all architectures. Extensive documentation is available in various other formats including DVI, PostScript and HTML; see below. </p>
<p> Each of GHC&#8217;s command line options is classified as either <i>static</i> or <i>dynamic</i>. A static flag may only be specified on the command line, whereas a dynamic flag may also be given in an OPTIONS pragma in a source file or set from the GHCi command-line with :set. </p>
<p> As a rule of thumb, all the language options are dynamic, as are the warning options and the debugging options. </p>
<p> The rest are static, with the notable exceptions of <code>-v</code>, <code>-cpp</code>, <code>-fasm</code>, <code>-fvia-C</code>, <code>-fllvm</code>, and &quot; -#include . The OPTIONS sections lists the status of each flag. </p>
<p> Common suffixes of file names for Haskell are:</p>
<dl>
<dt><code>.hs</code></p>
<dd> Haskell source code; preprocess, compile</p>
<dt><code>.lhs</code></p>
<dd> literate Haskell source; unlit, preprocess, compile</p>
<dt><code>.hi</code></p>
<dd> Interface file; contains information about exported symbols</p>
<dt><code>.hc</code></p>
<dd> intermediate C files</p>
<dt><code>.</code><i>x</i><code>_o</code></p>
<dd> way <i>x</i> object files; common ways are: <code>p</code>, <code>u</code>, <code>s</code></p>
<dt><code>.</code><i>x</i><code>_hi</code></p>
<dd> way <i>x</i> interface files </p>
</dl>
<h2>OPTIONS</h2>
<h3>Help and verbosity options</h3>
<p> -? -help -v -v<i>n</i> -V &#8211;supported-extensions or &#8211;supported-languages &#8211;info &#8211;version &#8211;numeric-version &#8211;print-libdir -ferror-spans -H<i>size</i> -Rghc-timing </p>
<h3>Which phases to run</h3>
<p> -E -C -S -c -x <i>suffix</i> </p>
<h3>Alternative modes of operation</h3>
<p> &#8211;interactive &#8211;make -e expr -M </p>
<h3>Redirecting output</h3>
<p> -hcsuf <i>suffix</i> -hidir <i>dir</i> -hisuf <i>suffix</i> -o <i>filename</i> -odir <i>dir</i> -ohi <i>filename</i> -osuf <i>suffix</i> -stubdir <i>dir</i> -dumpdir <i>dir</i> -outputdir <i>dir</i> </p>
<h3>Keeping intermediate files</h3>
<p> -keep-hc-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-hc-files&nbsp;<wbr>&nbsp;<wbr>-keep-llvm-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-llvm-files&nbsp;<wbr>&nbsp;<wbr>-keep-s-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-s-files&nbsp;<wbr>&nbsp;<wbr>-keep-tmp-files&nbsp;<wbr>&nbsp;<wbr> </p>
<h3>Temporary files</h3>
<p> -tmpdir </p>
<h3>Finding imports</h3>
<p> -i<i>dir1</i>:<i>dir2</i>:&#8230; -i </p>
<h3>Interface file options</h3>
<p> -ddump-hi -ddump-hi-diffs -ddump-minimal-imports &#8211;show-iface <i>file</i> </p>
<h3>Recompilation checking</h3>
<p> -fforce-recomp -fno-force-recomp </p>
<h3>Interactive-mode options</h3>
<p> -ignore-dot-ghci -ghci-script -fbreak-on-exception -fno-break-on-exception -fbreak-on-error -fno-break-on-error -fprint-evld-with-show -fno-print-evld-with-show -fprint-bind-result -fno-print-bind-result -fno-print-bind-contents -fno-implicit-import-qualified -interactive-print </p>
<h3>Packages</h3>
<p> -package-name <i>P</i> -package <i>P</i> -hide-all-packages -hide-package <i>name</i> -ignore-package <i>name</i> -package-db <i>file</i> -clear-package-db -no-global-package-db -global-package-db -no-user-package-db -user-package-db -no-auto-link-packages -trust <i>P</i> -distrust <i>P</i> -distrust-all </p>
<h3>Language options</h3>
<p> -fglasgow-exts -fno-glasgow-exts -XOverlappingInstances -XNoOverlappingInstances -XIncoherentInstances -XNoIncoherentInstances -XUndecidableInstances -XNoUndecidableInstances -fcontext-stack=N<i>n</i> -XArrows -XNoArrows -XDisambiguateRecordFields -XNoDisambiguateRecordFields -XForeignFunctionInterface -XNoForeignFunctionInterface -XGenerics -XNoGenerics -XImplicitParams -XNoImplicitParams -firrefutable-tuples -fno-irrefutable-tuples -XNoImplicitPrelude -XImplicitPrelude -XRebindableSyntax -XNoRebindableSyntax -XNoMonomorphismRestriction -XMonomorphismRrestriction -XNoNPlusKPatterns -XNPlusKPatterns -XNoTraditionalRecordSyntax -XTraditionalRecordSyntax -XNoMonoPatBinds -XMonoPatBinds -XRelaxedPolyRec -XNoRelaxedPolyRec -XExtendedDefaultRules -XNoExtendedDefaultRules -XOverloadedStrings -XNoOverloadedStrings -XGADTs -XNoGADTs -XGADTSyntax -XNoGADTSyntax -XTypeFamilies -XNoTypeFamilies -XConstraintKinds -XNoConstraintKinds -XDataKinds -XNoDataKinds -XPolyKinds -XNoPolyKinds -XScopedTypeVariables -XNoScopedTypeVariables -XMonoLocalBinds -XNoMonoLocalBinds -XTemplateHaskell -XNoTemplateHaskell -XQuasiQuotes -XNoQuasiQuotes -XBangPatterns -XNoBangPatterns -XCPP -XNoCPP -XPatternGuards -XNoPatternGuards -XViewPatterns -XNoViewPatterns -XUnicodeSyntax -XNoUnicodeSyntax -XMagicHash -XNoMagicHash -XExplicitForAll -XNoExplicitForAll -XPolymorphicComponents -XNoPolymorphicComponents -XRank2Types -XNoRank2Types -XRankNTypes -XNoRankNTypes -XImpredicativeTypes -XNoImpredicativeTypes -XExistentialQuantification -XNoExistentialQuantification -XKindSignatures -XNoKindSignatures -XEmptyDataDecls -XNoEmptyDataDecls -XParallelListComp -XNoParallelListComp -XTransformListComp -XNoTransformListComp -XMonadComprehensions -XNoMonadComprehensions -XUnliftedFFITypes -XNoUnliftedFFITypes -XInterruptibleFFI -XNoInterruptibleFFI -XLiberalTypeSynonyms -XNoLiberalTypeSynonyms -XTypeOperators -XNoTypeOperators -XExplicitNamespaces -XNoExplicitNamespaces -XRecursiveDo -XNoRecursiveDo -XParallelArrays -XNoParallelArrays -XRecordWildCards -XNoRecordWildCards -XNamedFieldPuns -XNoNamedFieldPuns -XDisambiguateRecordFields -XNoDisambiguateRecordFields -XUnboxedTuples -XNoUnboxedTuples -XStandaloneDeriving -XNoStandaloneDeriving -XDeriveDataTypeable -XNoDeriveDataTypeable -XDeriveGeneric -XNoDeriveGeneric -XGeneralizedNewtypeDeriving -XNoGeneralizedNewtypeDeriving -XTypeSynonymInstances -XNoTypeSynonymInstances -XFlexibleContexts -XNoFlexibleContexts -XFlexibleInstances -XNoFlexibleInstances -XConstrainedClassMethods -XNoConstrainedClassMethods -XDefaultSignatures -XNoDefaultSignatures -XMultiParamTypeClasses -XNoMultiParamTypeClasses -XFunctionalDependencies -XNoFunctionalDependencies -XPackageImports -XNoPackageImports -XLambdaCase -XNoLambdaCase -XMultiWayIf -XNoMultiWayIf -XSafe -XTrustworthy -XUnsafe -fpackage-trust </p>
<h3>Warnings</h3>
<p> -W -w -w -Wall -w -Werror -Wwarn -fdefer-type-errors -fno-defer-type-errors -fhelpful-errors -fno-helpful-errors -fwarn-deprecated-flags -fno-warn-deprecated-flags -fwarn-duplicate-exports -fno-warn-duplicate-exports -fwarn-hi-shadowing -fno-warn-hi-shadowing -fwarn-identities -fno-warn-identities -fwarn-implicit-prelude -fno-warn-implicit-prelude -fwarn-incomplete-patterns -fno-warn-incomplete-patterns -fwarn-incomplete-uni-patterns -fno-warn-incomplete-uni-patterns -fwarn-incomplete-record-updates -fno-warn-incomplete-record-updates -fwarn-lazy-unlifted-bindings -fno-warn-lazy-unlifted-bindings -fwarn-missing-fields -fno-warn-missing-fields -fwarn-missing-import-lists -fnowarn-missing-import-lists -fwarn-missing-methods -fno-warn-missing-methods -fwarn-missing-signatures -fno-warn-missing-signatures -fwarn-missing-local-sigs -fno-warn-missing-local-sigs -fwarn-monomorphism-restriction -fno-warn-monomorphism-restriction -fwarn-name-shadowing -fno-warn-name-shadowing -fwarn-orphans, -fwarn-auto-orphans -fno-warn-orphans, -fno-warn-auto-orphans -fwarn-overlapping-patterns -fno-warn-overlapping-patterns -fwarn-tabs -fno-warn-tabs -fwarn-type-defaults -fno-warn-type-defaults -fwarn-unrecognised-pragmas -fno-warn-unrecognised-pragmas -fwarn-unused-binds -fno-warn-unused-binds -fwarn-unused-imports -fno-warn-unused-imports -fwarn-unused-matches -fno-warn-unused-matches -fwarn-unused-do-bind -fno-warn-unused-do-bind -fwarn-wrong-do-bind -fno-warn-wrong-do-bind -fwarn-unsafe -fno-warn-unsafe -fwarn-safe -fno-warn-safe -fwarn-warnings-deprecations -fno-warn-warnings-deprecations </p>
<h3>Optimisation levels</h3>
<p> -O -O0 -O<i>n</i> -O0 </p>
<h3>Individual optimisations</h3>
<p> -fcase-merge -fno-case-merge -fcse -fdicts-strict -fno-dicts-strict -fdo-eta-reduction -fno-do-eta-reduction -fdo-lambda-eta-expansion -fno-do-lambda-eta-expansion -feager-blackholing -fenable-rewrite-rules -fno-enable-rewrite-rules -fvectorise -fno-vectorise -favoid-vect -fno-avoid-vect -fexcess-precision -fno-excess-precision -ffloat-in -ffull-laziness -fignore-asserts -fno-ignore-asserts -fignore-interface-pragmas -fno-ignore-interface-pragmas -fliberate-case -fliberate-case-threshold=<i>n</i> -fno-liberate-case-threshold -fmax-simplifier-iterations -fmax-worker-args -fno-opt-coercion -fno-pre-inlining -fno-state-hack -fpedantic-bottoms -fno-pedantic-bottoms -fomit-interface-pragmas -fno-omit-interface-pragmas -fsimplifier-phases -fsimpl-tick-factor=n -fspec-constr -fspec-constr-threshold=<i>n</i> -fno-spec-constr-threshold -fspec-constr-count=<i>n</i> -fno-spec-constr-count -fspecialise -fstrictness -fstrictness=before=<i>n</i> -fstatic-argument-transformation -funbox-strict-fields -fno-unbox-strict-fields -funfolding-creation-threshold -fno-unfolding-creation-threshold -funfolding-fun-discount -fno-unfolding-fun-discount -funfolding-keeness-factor -fno-unfolding-keeness-factor -funfolding-use-threshold -fno-unfolding-use-threshold </p>
<h3>Profiling options</h3>
<p> -prof -fprof-auto -fno-prof-auto -fprof-auto-top -fno-prof-auto -fprof-auto-exported -fno-prof-auto -fprof-cafs -fno-prof-cafs -fno-prof-count-entries -fprof-count-entries -ticky </p>
<h3>Program coverage options</h3>
<p> -fhpc -hpcdir dir </p>
<h3>Haskell pre-processor options</h3>
<p> -F </p>
<h3>C pre-processor options</h3>
<p> -cpp -D<i>symbol</i>=<i>value</i> -U -U<i>symbol</i> -I<i>dir</i> </p>
<h3>Code generation options</h3>
<p> -fasm -fllvm -fno-code -fbyte-code -fobject-code </p>
<h3>Linking options</h3>
<p> -shared -fPIC -dynamic -dynload -framework <i>name</i> -framework-path <i>name</i> -l<i>lib</i> -L<i>dir</i> -main-is &#8211;mk-dll -no-hs-main -rtsopts, -rtsopts={none,some,all} -with-rtsopts=opts -no-link -split-objs -static -threaded -debug -eventlog -fno-gen-manifest -fno-embed-manifest -fno-shared-implib -dylib-install-name <i>path</i> </p>
<h3>Plugin options</h3>
<p> -fplugin=<i>module</i> -fplugin-opt=<i>module:args</i> </p>
<h3>Replacing phases</h3>
<p> -pgmL <i>cmd</i> -pgmP <i>cmd</i> -pgmc <i>cmd</i> -pgms <i>cmd</i> -pgma <i>cmd</i> -pgml <i>cmd</i> -pgmdll <i>cmd</i> -pgmF <i>cmd</i> -pgmwindres <i>cmd</i> </p>
<h3>Forcing options to particular phases</h3>
<p> -optL <i>option</i> -optP <i>option</i> -optF <i>option</i> -optc <i>option</i> -optlo <i>option</i> -optlc <i>option</i> -optm <i>option</i> -opta <i>option</i> -optl <i>option</i> -optdll <i>option</i> -optwindres <i>option</i> </p>
<h3>Platform-specific options</h3>
<p> -msse2 -monly-[432]-regs </p>
<h3>External core file options</h3>
<p> -fext-core </p>
<h3>Compiler debugging options</h3>
<p> -dcore-lint -ddump-to-file -ddump-asm -ddump-bcos -ddump-cmm -ddump-core-stats -ddump-cpranal -ddump-cse -ddump-deriv -ddump-ds -ddump-flatC -ddump-foreign -ddump-hpc -ddump-inlinings -ddump-llvm -ddump-occur-anal -ddump-opt-cmm -ddump-parsed -ddump-prep -ddump-rn -ddump-rule-firings -ddump-rule-rewrites -ddump-rules -ddump-vect -ddump-simpl -ddump-simpl-phases -ddump-simpl-iterations -ddump-spec -ddump-splices -ddump-stg -ddump-stranal -ddump-tc -ddump-types -ddump-worker-wrapper -ddump-if-trace -ddump-tc-trace -ddump-vt-trace -ddump-rn-trace -ddump-rn-stats -ddump-simpl-stats -dno-debug-output -dppr-debug -dppr-noprags -dppr-user-length -dppr-colsNNN -dppr-case-as-let -dsuppress-all -dsuppress-uniques -dsuppress-idinfo -dsuppress-module-prefixes -dsuppress-type-signatures -dsuppress-type-applications -dsuppress-coercions -dsource-stats -dcmm-lint -dstg-lint -dstg-stats -dverbose-core2core -dverbose-stg2stg -dshow-passes -dfaststring-stats </p>
<h3>Misc compiler options</h3>
<p> -fno-hi-version-check -dno-black-holing -fhistory-size -funregisterised -fno-ghci-history -fno-ghci-sandbox </p>
<h2>HELP AND VERBOSITY OPTIONS</h2>
<dl>
<dt><code>-?</code></p>
<dd> help [mode] </p>
<dt><code>-help</code></p>
<dd> help [mode] </p>
<dt><code>-v</code></p>
<dd> verbose mode (equivalent to <code>-v3</code>) [dynamic] </p>
<dt><code>-v</code><i>n</i></p>
<dd> set verbosity level [dynamic] </p>
<dt><code>-V</code></p>
<dd> display GHC version [mode] </p>
<dt><code>&#8211;supported-extensions</code> or <code>&#8211;supported-languages</code></p>
<dd> display the supported languages and language extensions [mode] </p>
<dt><code>&#8211;info</code></p>
<dd> display information about the compiler [mode] </p>
<dt><code>&#8211;version</code></p>
<dd> display GHC version [mode] </p>
<dt><code>&#8211;numeric-version</code></p>
<dd> display GHC version (numeric only) [mode] </p>
<dt><code>&#8211;print-libdir</code></p>
<dd> display GHC library directory [mode] </p>
<dt><code>-ferror-spans</code></p>
<dd> output full span in error messages [static] </p>
<dt><code>-H</code><i>size</i></p>
<dd> Set the minimum heap size to <i>size</i> [static] </p>
<dt><code>-Rghc-timing</code></p>
<dd> Summarise timing stats for GHC (same as +RTS -tstderr) [static] </p>
</dl>
<h2>WHICH PHASES TO RUN</h2>
<dl>
<dt><code>-E</code></p>
<dd> Stop after preprocessing (.hspp file) [mode] </p>
<dt><code>-C</code></p>
<dd> Stop after generating C (.hc file) [mode] </p>
<dt><code>-S</code></p>
<dd> Stop after generating assembly (.s file) [mode] </p>
<dt><code>-c</code></p>
<dd> Do not link [dynamic] </p>
<dt><code>-x</code> <i>suffix</i></p>
<dd> Override default behaviour for source files [static] </p>
</dl>
<h2>ALTERNATIVE MODES OF OPERATION</h2>
<dl>
<dt><code>&#8211;interactive</code></p>
<dd> Interactive mode &#8211; normally used by just running ghci; see for details. [mode] </p>
<dt><code>&#8211;make</code></p>
<dd> Build a multi-module Haskell program, automatically figuring out dependencies. Likely to be much easier, and faster, than using make; see for details.. [mode] </p>
<dt><code>-e expr</code></p>
<dd> Evaluate <i>expr</i>; see for details. [mode] </p>
<dt><code>-M</code></p>
<dd> Generate dependency information suitable for use in a Makefile; see for details. [mode] </p>
</dl>
<h2>REDIRECTING OUTPUT</h2>
<dl>
<dt><code>-hcsuf</code> <i>suffix</i></p>
<dd> set the suffix to use for intermediate C files [dynamic] </p>
<dt><code>-hidir</code> <i>dir</i></p>
<dd> set directory for interface files [dynamic] </p>
<dt><code>-hisuf</code> <i>suffix</i></p>
<dd> set the suffix to use for interface files [dynamic] </p>
<dt><code>-o</code> <i>filename</i></p>
<dd> set output filename [dynamic] </p>
<dt><code>-odir</code> <i>dir</i></p>
<dd> set directory for object files [dynamic] </p>
<dt><code>-ohi</code> <i>filename</i></p>
<dd> set the filename in which to put the interface [dynamic] </p>
<dt><code>-osuf</code> <i>suffix</i></p>
<dd> set the output file suffix [dynamic] </p>
<dt><code>-stubdir</code> <i>dir</i></p>
<dd> redirect FFI stub files [dynamic] </p>
<dt><code>-dumpdir</code> <i>dir</i></p>
<dd> redirect dump files [dynamic] </p>
<dt><code>-outputdir</code> <i>dir</i></p>
<dd> set output directory [dynamic] </p>
</dl>
<h2>KEEPING INTERMEDIATE FILES</h2>
<dl>
<dt><code>-keep-hc-file</code> or</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-hc-files</code>&nbsp;<wbr> retain intermediate .hc files [dynamic] </p>
<dt><code>-keep-llvm-file</code> or</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-llvm-files</code>&nbsp;<wbr> retain intermediate LLVM .ll files [dynamic] </p>
<dt><code>-keep-s-file</code> or</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-s-files</code>&nbsp;<wbr> retain intermediate .s files [dynamic] </p>
<dt><code>-keep-tmp-files</code></p>
<dd> retain all intermediate temporary files [dynamic] </p>
</dl>
<h2>TEMPORARY FILES</h2>
<dl>
<dt><code>-tmpdir</code></p>
<dd> set the directory for temporary files [dynamic] </p>
</dl>
<h2>FINDING IMPORTS</h2>
<dl>
<dt><code>-i</code><i>dir1</i>:<i>dir2</i>:&#8230;</p>
<dd> add <i>dir</i>, <i>dir2</i>, etc. to import path [static/:set] </p>
<dt><code>-i</code></p>
<dd> Empty the import directory list [static/:set] </p>
</dl>
<h2>INTERFACE FILE OPTIONS</h2>
<dl>
<dt><code>-ddump-hi</code></p>
<dd> Dump the new interface to stdout [dynamic] </p>
<dt><code>-ddump-hi-diffs</code></p>
<dd> Show the differences vs. the old interface [dynamic] </p>
<dt><code>-ddump-minimal-imports</code></p>
<dd> Dump a minimal set of imports [dynamic] </p>
<dt><code>&#8211;show-iface</code> <i>file</i></p>
<dd> See . [] </p>
</dl>
<h2>RECOMPILATION CHECKING</h2>
<dl>
<dt><code>-fforce-recomp</code></p>
<dd> Turn off recompilation checking; implied by any <code>-ddump-X</code> option [dynamic] </p>
</dl>
<h2>INTERACTIVE-MODE OPTIONS</h2>
<dl>
<dt><code>-ignore-dot-ghci</code></p>
<dd> Disable reading of .ghci files [dynamic] </p>
<dt><code>-ghci-script</code></p>
<dd> Read additional .ghci files [dynamic] </p>
<dt><code>-fbreak-on-exception</code></p>
<dd> Break on any exception thrown [dynamic] </p>
<dt><code>-fbreak-on-error</code></p>
<dd> Break on uncaught exceptions and errors [dynamic] </p>
<dt><code>-fprint-evld-with-show</code></p>
<dd> Enable usage of Show instances in :print [dynamic] </p>
<dt><code>-fprint-bind-result</code></p>
<dd> Turn on printing of binding results in GHCi [dynamic] </p>
<dt><code>-fno-print-bind-contents</code></p>
<dd> Turn off printing of binding contents in GHCi [dynamic] </p>
<dt><code>-fno-implicit-import-qualified</code></p>
<dd> Turn off implicit qualified import of everything in GHCi [dynamic] </p>
<dt><code>-interactive-print</code></p>
<dd> Select the function to use for printing evaluated expressions in GHCi [dynamic] </p>
</dl>
<h2>PACKAGES</h2>
<dl>
<dt><code>-package-name</code> <i>P</i></p>
<dd> Compile to be part of package <i>P</i> [static] </p>
<dt><code>-package</code> <i>P</i></p>
<dd> Expose package <i>P</i> [static/:set] </p>
<dt><code>-hide-all-packages</code></p>
<dd> Hide all packages by default [static] </p>
<dt><code>-hide-package</code> <i>name</i></p>
<dd> Hide package <i>P</i> [static/:set] </p>
<dt><code>-ignore-package</code> <i>name</i></p>
<dd> Ignore package <i>P</i> [static/:set] </p>
<dt><code>-package-db</code> <i>file</i></p>
<dd> Add <i>file</i> to the package db stack. [static] </p>
<dt><code>-clear-package-db</code></p>
<dd> Clear the package db stack. [static] </p>
<dt><code>-no-global-package-db</code></p>
<dd> Remove the global package db from the stack. [static] </p>
<dt><code>-global-package-db</code></p>
<dd> Add the global package db to the stack. [static] </p>
<dt><code>-no-user-package-db</code></p>
<dd> Remove the user&#8217;s package db from the stack. [static] </p>
<dt><code>-user-package-db</code></p>
<dd> Add the user&#8217;s package db to the stack. [static] </p>
<dt><code>-no-auto-link-packages</code></p>
<dd> Don&#8217;t automatically link in the haskell98 package. [dynamic] </p>
<dt><code>-trust</code> <i>P</i></p>
<dd> Expose package <i>P</i> and set it to be trusted [static/:set] </p>
<dt><code>-distrust</code> <i>P</i></p>
<dd> Expose package <i>P</i> and set it to be distrusted [static/:set] </p>
<dt><code>-distrust-all</code></p>
<dd> Distrust all packages by default [static/:set] </p>
</dl>
<h2>LANGUAGE OPTIONS</h2>
<dl>
<dt><code>-fglasgow-exts</code></p>
<dd> Enable most language extensions; see for exactly which ones. [dynamic] </p>
<dt><code>-XOverlappingInstances</code></p>
<dd> Enable overlapping instances [dynamic] </p>
<dt><code>-XIncoherentInstances</code></p>
<dd> Enable incoherent instances. Implies <code>-XOverlappingInstances</code> [dynamic] </p>
<dt><code>-XUndecidableInstances</code></p>
<dd> Enable undecidable instances [dynamic] </p>
<dt><code>-fcontext-stack=N</code><i>n</i></p>
<dd> set the limit for context reduction. Default is 20. [dynamic] </p>
<dt><code>-XArrows</code></p>
<dd> Enable arrow notation extension [dynamic] </p>
<dt><code>-XDisambiguateRecordFields</code></p>
<dd> Enable record field disambiguation [dynamic] </p>
<dt><code>-XForeignFunctionInterface</code></p>
<dd> Enable foreign function interface (implied by <code>-fglasgow-exts</code>) [dynamic] </p>
<dt><code>-XGenerics</code></p>
<dd> Deprecated, does nothing. No longer enables generic classes. See also GHC&#8217;s support for generic programming. [dynamic] </p>
<dt><code>-XImplicitParams</code></p>
<dd> Enable Implicit Parameters. Implied by <code>-fglasgow-exts</code>. [dynamic] </p>
<dt><code>-firrefutable-tuples</code></p>
<dd> Make tuple pattern matching irrefutable [dynamic] </p>
<dt><code>-XNoImplicitPrelude</code></p>
<dd> Don&#8217;t implicitly import Prelude [dynamic] </p>
<dt><code>-XRebindableSyntax</code></p>
<dd> Employ rebindable syntax [dynamic] </p>
<dt><code>-XNoMonomorphismRestriction</code></p>
<dd> Disable the monomorphism restriction [dynamic] </p>
<dt><code>-XNoNPlusKPatterns</code></p>
<dd> Disable support for n+k patterns [dynamic] </p>
<dt><code>-XNoTraditionalRecordSyntax</code></p>
<dd> Disable support for traditional record syntax (as supported by Haskell 98) C {f = x} [dynamic] </p>
<dt><code>-XNoMonoPatBinds</code></p>
<dd> Make pattern bindings polymorphic [dynamic] </p>
<dt><code>-XRelaxedPolyRec</code></p>
<dd> Relaxed checking for mutually-recursive polymorphic functions [dynamic] </p>
<dt><code>-XExtendedDefaultRules</code></p>
<dd> Use GHCi&#8217;s extended default rules in a normal module [dynamic] </p>
<dt><code>-XOverloadedStrings</code></p>
<dd> Enable overloaded string literals. [dynamic] </p>
<dt><code>-XGADTs</code></p>
<dd> Enable generalised algebraic data types. [dynamic] </p>
<dt><code>-XGADTSyntax</code></p>
<dd> Enable generalised algebraic data type syntax. [dynamic] </p>
<dt><code>-XTypeFamilies</code></p>
<dd> Enable type families. [dynamic] </p>
<dt><code>-XConstraintKinds</code></p>
<dd> Enable a kind of constraints. [dynamic] </p>
<dt><code>-XDataKinds</code></p>
<dd> Enable datatype promotion. [dynamic] </p>
<dt><code>-XPolyKinds</code></p>
<dd> Enable kind polymorphism. Implies <code>-XKindSignatures</code>. [dynamic] </p>
<dt><code>-XScopedTypeVariables</code></p>
<dd> Enable lexically-scoped type variables. Implied by <code>-fglasgow-exts</code>. [dynamic] </p>
<dt><code>-XMonoLocalBinds</code></p>
<dd> Enable do not generalise local bindings. [dynamic] </p>
<dt><code>-XTemplateHaskell</code></p>
<dd> Enable Template Haskell. No longer implied by <code>-fglasgow-exts</code>. [dynamic] </p>
<dt><code>-XQuasiQuotes</code></p>
<dd> Enable quasiquotation. [dynamic] </p>
<dt><code>-XBangPatterns</code></p>
<dd> Enable bang patterns. [dynamic] </p>
<dt><code>-XCPP</code></p>
<dd> Enable the C preprocessor. [dynamic] </p>
<dt><code>-XPatternGuards</code></p>
<dd> Enable pattern guards. [dynamic] </p>
<dt><code>-XViewPatterns</code></p>
<dd> Enable view patterns. [dynamic] </p>
<dt><code>-XUnicodeSyntax</code></p>
<dd> Enable unicode syntax. [dynamic] </p>
<dt><code>-XMagicHash</code></p>
<dd> Allow &quot;#&quot; as a postfix modifier on identifiers. [dynamic] </p>
<dt><code>-XExplicitForAll</code></p>
<dd> Enable explicit universal quantification. Implied by <code>-XScopedTypeVariables</code>, <code>-XLiberalTypeSynonyms</code>, <code>-XRank2Types</code>, <code>-XRankNTypes</code>, <code>-XPolymorphicComponents</code>, <code>-XExistentialQuantification</code> [dynamic] </p>
<dt><code>-XPolymorphicComponents</code></p>
<dd> Enable polymorphic components for data constructors. [dynamic] </p>
<dt><code>-XRank2Types</code></p>
<dd> Enable rank-2 types. [dynamic] </p>
<dt><code>-XRankNTypes</code></p>
<dd> Enable rank-N types. [dynamic] </p>
<dt><code>-XImpredicativeTypes</code></p>
<dd> Enable impredicative types. [dynamic] </p>
<dt><code>-XExistentialQuantification</code></p>
<dd> Enable existential quantification. [dynamic] </p>
<dt><code>-XKindSignatures</code></p>
<dd> Enable kind signatures. [dynamic] </p>
<dt><code>-XEmptyDataDecls</code></p>
<dd> Enable empty data declarations. [dynamic] </p>
<dt><code>-XParallelListComp</code></p>
<dd> Enable parallel list comprehensions. [dynamic] </p>
<dt><code>-XTransformListComp</code></p>
<dd> Enable generalised list comprehensions. [dynamic] </p>
<dt><code>-XMonadComprehensions</code></p>
<dd> Enable monad comprehensions. [dynamic] </p>
<dt><code>-XUnliftedFFITypes</code></p>
<dd> Enable unlifted FFI types. [dynamic] </p>
<dt><code>-XInterruptibleFFI</code></p>
<dd> Enable interruptible FFI. [dynamic] </p>
<dt><code>-XLiberalTypeSynonyms</code></p>
<dd> Enable liberalised type synonyms. [dynamic] </p>
<dt><code>-XTypeOperators</code></p>
<dd> Enable type operators. [dynamic] </p>
<dt><code>-XExplicitNamespaces</code></p>
<dd> Enable using the keyword type to specify the namespace of entries in imports and exports. [dynamic] </p>
<dt><code>-XRecursiveDo</code></p>
<dd> Enable recursive do (mdo) notation. [dynamic] </p>
<dt><code>-XParallelArrays</code></p>
<dd> Enable parallel arrays. [dynamic] </p>
<dt><code>-XRecordWildCards</code></p>
<dd> Enable record wildcards. [dynamic] </p>
<dt><code>-XNamedFieldPuns</code></p>
<dd> Enable record puns. [dynamic] </p>
<dt><code>-XDisambiguateRecordFields</code></p>
<dd> Enable record field disambiguation. [dynamic] </p>
<dt><code>-XUnboxedTuples</code></p>
<dd> Enable unboxed tuples. [dynamic] </p>
<dt><code>-XStandaloneDeriving</code></p>
<dd> Enable standalone deriving. [dynamic] </p>
<dt><code>-XDeriveDataTypeable</code></p>
<dd> Enable deriving for the Data and Typeable classes. [dynamic] </p>
<dt><code>-XDeriveGeneric</code></p>
<dd> Enable deriving for the Generic class. [dynamic] </p>
<dt><code>-XGeneralizedNewtypeDeriving</code></p>
<dd> Enable newtype deriving. [dynamic] </p>
<dt><code>-XTypeSynonymInstances</code></p>
<dd> Enable type synonyms in instance heads. [dynamic] </p>
<dt><code>-XFlexibleContexts</code></p>
<dd> Enable flexible contexts. [dynamic] </p>
<dt><code>-XFlexibleInstances</code></p>
<dd> Enable flexible instances. Implies <code>-XTypeSynonymInstances</code> [dynamic] </p>
<dt><code>-XConstrainedClassMethods</code></p>
<dd> Enable constrained class methods. [dynamic] </p>
<dt><code>-XDefaultSignatures</code></p>
<dd> Enable default signatures. [dynamic] </p>
<dt><code>-XMultiParamTypeClasses</code></p>
<dd> Enable multi parameter type classes. [dynamic] </p>
<dt><code>-XFunctionalDependencies</code></p>
<dd> Enable functional dependencies. [dynamic] </p>
<dt><code>-XPackageImports</code></p>
<dd> Enable package-qualified imports. [dynamic] </p>
<dt><code>-XLambdaCase</code></p>
<dd> Enable lambda-case expressions. [dynamic] </p>
<dt><code>-XMultiWayIf</code></p>
<dd> Enable multi-way if-expressions. [dynamic] </p>
<dt><code>-XSafe</code></p>
<dd> Enable the Safe Haskell Safe mode. [dynamic] </p>
<dt><code>-XTrustworthy</code></p>
<dd> Enable the Safe Haskell Trustworthy mode. [dynamic] </p>
<dt><code>-XUnsafe</code></p>
<dd> Enable Safe Haskell Unsafe mode. [dynamic] </p>
<dt><code>-fpackage-trust</code></p>
<dd> Enable Safe Haskell trusted package requirement for trustworty modules. [dynamic] </p>
</dl>
<h2>WARNINGS</h2>
<dl>
<dt><code>-W</code></p>
<dd> enable normal warnings [dynamic] </p>
<dt><code>-w</code></p>
<dd> disable all warnings [dynamic] </p>
<dt><code>-Wall</code></p>
<dd> enable almost all warnings (details in ) [dynamic] </p>
<dt><code>-Werror</code></p>
<dd> make warnings fatal [dynamic] </p>
<dt><code>-Wwarn</code></p>
<dd> make warnings non-fatal [dynamic] </p>
<dt><code>-fdefer-type-errors</code></p>
<dd> Defer as many type errors as possible until runtime. [dynamic] </p>
<dt><code>-fhelpful-errors</code></p>
<dd> Make suggestions for mis-spelled names. [dynamic] </p>
<dt><code>-fwarn-deprecated-flags</code></p>
<dd> warn about uses of commandline flags that are deprecated [dynamic] </p>
<dt><code>-fwarn-duplicate-exports</code></p>
<dd> warn when an entity is exported multiple times [dynamic] </p>
<dt><code>-fwarn-hi-shadowing</code></p>
<dd> warn when a .hi file in the current directory shadows a library [dynamic] </p>
<dt><code>-fwarn-identities</code></p>
<dd> warn about uses of Prelude numeric conversions that are probably the identity (and hence could be omitted) [dynamic] </p>
<dt><code>-fwarn-implicit-prelude</code></p>
<dd> warn when the Prelude is implicitly imported [dynamic] </p>
<dt><code>-fwarn-incomplete-patterns</code></p>
<dd> warn when a pattern match could fail [dynamic] </p>
<dt><code>-fwarn-incomplete-uni-patterns</code></p>
<dd> warn when a pattern match in a lambda expression or pattern binding could fail [dynamic] </p>
<dt><code>-fwarn-incomplete-record-updates</code></p>
<dd> warn when a record update could fail [dynamic] </p>
<dt><code>-fwarn-lazy-unlifted-bindings</code></p>
<dd> warn when a pattern binding looks lazy but must be strict [dynamic] </p>
<dt><code>-fwarn-missing-fields</code></p>
<dd> warn when fields of a record are uninitialised [dynamic] </p>
<dt><code>-fwarn-missing-import-lists</code></p>
<dd> warn when an import declaration does not explicitly list all the names brought into scope [dynamic] </p>
<dt><code>-fwarn-missing-methods</code></p>
<dd> warn when class methods are undefined [dynamic] </p>
<dt><code>-fwarn-missing-signatures</code></p>
<dd> warn about top-level functions without signatures [dynamic] </p>
<dt><code>-fwarn-missing-local-sigs</code></p>
<dd> warn about polymorphic local bindings without signatures [dynamic] </p>
<dt><code>-fwarn-monomorphism-restriction</code></p>
<dd> warn when the Monomorphism Restriction is applied [dynamic] </p>
<dt><code>-fwarn-name-shadowing</code></p>
<dd> warn when names are shadowed [dynamic] </p>
<dt><code>-fwarn-orphans, -fwarn-auto-orphans</code></p>
<dd> warn when the module contains orphan instance declarations or rewrite rules [dynamic] </p>
<dt><code>-fwarn-overlapping-patterns</code></p>
<dd> warn about overlapping patterns [dynamic] </p>
<dt><code>-fwarn-tabs</code></p>
<dd> warn if there are tabs in the source file [dynamic] </p>
<dt><code>-fwarn-type-defaults</code></p>
<dd> warn when defaulting happens [dynamic] </p>
<dt><code>-fwarn-unrecognised-pragmas</code></p>
<dd> warn about uses of pragmas that GHC doesn&#8217;t recognise [dynamic] </p>
<dt><code>-fwarn-unused-binds</code></p>
<dd> warn about bindings that are unused [dynamic] </p>
<dt><code>-fwarn-unused-imports</code></p>
<dd> warn about unnecessary imports [dynamic] </p>
<dt><code>-fwarn-unused-matches</code></p>
<dd> warn about variables in patterns that aren&#8217;t used [dynamic] </p>
<dt><code>-fwarn-unused-do-bind</code></p>
<dd> warn about do bindings that appear to throw away values of types other than () [dynamic] </p>
<dt><code>-fwarn-wrong-do-bind</code></p>
<dd> warn about do bindings that appear to throw away monadic values that you should have bound instead [dynamic] </p>
<dt><code>-fwarn-unsafe</code></p>
<dd> warn if the module being compiled is regarded to be unsafe. Should be used to check the safety status of modules when using safe inference. [dynamic] </p>
<dt><code>-fwarn-safe</code></p>
<dd> warn if the module being compiled is regarded to be safe. Should be used to check the safety status of modules when using safe inference. [dynamic] </p>
<dt><code>-fwarn-warnings-deprecations</code></p>
<dd> warn about uses of functions &amp; types that have warnings or deprecated pragmas [dynamic] </p>
</dl>
<h2>OPTIMISATION LEVELS</h2>
<dl>
<dt><code>-O</code></p>
<dd> Enable default optimisation (level 1) [dynamic] </p>
<dt><code>-O</code><i>n</i></p>
<dd> Set optimisation level <i>n</i> [dynamic] </p>
</dl>
<h2>INDIVIDUAL OPTIMISATIONS</h2>
<dl>
<dt><code>-fcase-merge</code></p>
<dd> Enable case-merging. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fcse</code></p>
<dd> Turn on common sub-expression elimination. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fdicts-strict</code></p>
<dd> Make dictionaries strict [static] </p>
<dt><code>-fdo-eta-reduction</code></p>
<dd> Enable eta-reduction. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fdo-lambda-eta-expansion</code></p>
<dd> Enable lambda eta-reduction [dynamic] </p>
<dt><code>-feager-blackholing</code></p>
<dd> Turn on eager blackholing [dynamic] </p>
<dt><code>-fenable-rewrite-rules</code></p>
<dd> Switch on all rewrite rules (including rules generated by automatic specialisation of overloaded functions). Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fvectorise</code></p>
<dd> Enable vectorisation of nested data parallelism [dynamic] </p>
<dt><code>-favoid-vect</code></p>
<dd> Enable vectorisation avoidance (EXPERIMENTAL) [dynamic] </p>
<dt><code>-fexcess-precision</code></p>
<dd> Enable excess intermediate precision [dynamic] </p>
<dt><code>-ffloat-in</code></p>
<dd> Turn on the float-in transformation. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-ffull-laziness</code></p>
<dd> Turn on full laziness (floating bindings outwards). Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fignore-asserts</code></p>
<dd> Ignore assertions in the source [dynamic] </p>
<dt><code>-fignore-interface-pragmas</code></p>
<dd> Ignore pragmas in interface files [dynamic] </p>
<dt><code>-fliberate-case</code></p>
<dd> Turn on the liberate-case transformation. Implied by <code>-O2</code>. [dynamic] </p>
<dt><code>-fliberate-case-threshold</code>=<i>n</i></p>
<dd> Set the size threshold for the liberate-case transformation to <i>n</i> (default: 200) [static] </p>
<dt><code>-fmax-simplifier-iterations</code></p>
<dd> Set the max iterations for the simplifier [dynamic] </p>
<dt><code>-fmax-worker-args</code></p>
<dd> If a worker has that many arguments, none will be unpacked anymore (default: 10) [static] </p>
<dt><code>-fno-opt-coercion</code></p>
<dd> Turn off the coercion optimiser [static] </p>
<dt><code>-fno-pre-inlining</code></p>
<dd> Turn off pre-inlining [static] </p>
<dt><code>-fno-state-hack</code></p>
<dd> Turn off the &quot;state hack&quot; whereby any lambda with a real-world state token as argument is considered to be single-entry. Hence OK to inline things inside it. [static] </p>
<dt><code>-fpedantic-bottoms</code></p>
<dd> Make GHC be more precise about its treatment of bottom (but see also <code>-fno-state-hack</code>). In particular, GHC will not eta-expand through a case expression. [dynamic] </p>
<dt><code>-fomit-interface-pragmas</code></p>
<dd> Don&#8217;t generate interface pragmas [dynamic] </p>
<dt><code>-fsimplifier-phases</code></p>
<dd> Set the number of phases for the simplifier (default 2). Ignored with <code>-O0</code>. [dynamic] </p>
<dt><code>-fsimpl-tick-factor=n</code></p>
<dd> Set the percentage factor for simplifier ticks (default 100) [dynamic] </p>
<dt><code>-fspec-constr</code></p>
<dd> Turn on the SpecConstr transformation. Implied by <code>-O2</code>. [dynamic] </p>
<dt><code>-fspec-constr-threshold</code>=<i>n</i></p>
<dd> Set the size threshold for the SpecConstr transformation to <i>n</i> (default: 200) [static] </p>
<dt><code>-fspec-constr-count</code>=<i>n</i></p>
<dd> Set to <i>n</i> (default: 3) the maximum number of specialisations that will be created for any one function by the SpecConstr transformation [static] </p>
<dt><code>-fspecialise</code></p>
<dd> Turn on specialisation of overloaded functions. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fstrictness</code></p>
<dd> Turn on strictness analysis. Implied by <code>-O</code>. [dynamic] </p>
<dt><code>-fstrictness=before</code>=<i>n</i></p>
<dd> Run an additional strictness analysis before simplifier phase <i>n</i> [dynamic] </p>
<dt><code>-fstatic-argument-transformation</code></p>
<dd> Turn on the static argument transformation. Implied by <code>-O2</code>. [dynamic] </p>
<dt><code>-funbox-strict-fields</code></p>
<dd> Flatten strict constructor fields [dynamic] </p>
<dt><code>-funfolding-creation-threshold</code></p>
<dd> Tweak unfolding settings [static] </p>
<dt><code>-funfolding-fun-discount</code></p>
<dd> Tweak unfolding settings [static] </p>
<dt><code>-funfolding-keeness-factor</code></p>
<dd> Tweak unfolding settings [static] </p>
<dt><code>-funfolding-use-threshold</code></p>
<dd> Tweak unfolding settings [static] </p>
</dl>
<h2>PROFILING OPTIONS</h2>
<dl>
<dt><code>-prof</code></p>
<dd> Turn on profiling [static] </p>
<dt><code>-fprof-auto</code></p>
<dd> Auto-add SCCs to all bindings not marked INLINE [dynamic] </p>
<dt><code>-fprof-auto-top</code></p>
<dd> Auto-add SCCs to all top-level bindings not marked INLINE [dynamic] </p>
<dt><code>-fprof-auto-exported</code></p>
<dd> Auto-add SCCs to all exported bindings not marked INLINE [dynamic] </p>
<dt><code>-fprof-cafs</code></p>
<dd> Auto-add SCCs to all CAFs [dynamic] </p>
<dt><code>-fno-prof-count-entries</code></p>
<dd> Do not collect entry counts [dynamic] </p>
<dt><code>-ticky</code></p>
<dd> Turn on ticky-ticky profiling [static] </p>
</dl>
<h2>PROGRAM COVERAGE OPTIONS</h2>
<dl>
<dt><code>-fhpc</code></p>
<dd> Turn on Haskell program coverage instrumentation [static] </p>
<dt><code>-hpcdir dir</code></p>
<dd> Directory to deposit .mix files during compilation (default is .hpc) [dynamic] </p>
</dl>
<h2>HASKELL PRE-PROCESSOR OPTIONS</h2>
<dl>
<dt><code>-F</code></p>
<dd> Enable the use of a pre-processor (set with <code>-pgmF</code>) [dynamic] </p>
</dl>
<h2>C PRE-PROCESSOR OPTIONS</h2>
<dl>
<dt><code>-cpp</code></p>
<dd> Run the C pre-processor on Haskell source files [dynamic] </p>
<dt><code>-D</code><i>symbol</i>=<i>value</i></p>
<dd> Define a symbol in the C pre-processor [dynamic] </p>
<dt><code>-U</code><i>symbol</i></p>
<dd> Undefine a symbol in the C pre-processor [dynamic] </p>
<dt><code>-I</code><i>dir</i></p>
<dd> Add <i>dir</i> to the directory search list for #include files [dynamic] </p>
</dl>
<h2>CODE GENERATION OPTIONS</h2>
<dl>
<dt><code>-fasm</code></p>
<dd> Use the native code generator [dynamic] </p>
<dt><code>-fllvm</code></p>
<dd> Compile using the LLVM code generator [dynamic] </p>
<dt><code>-fno-code</code></p>
<dd> Omit code generation [dynamic] </p>
<dt><code>-fbyte-code</code></p>
<dd> Generate byte-code [dynamic] </p>
<dt><code>-fobject-code</code></p>
<dd> Generate object code [dynamic] </p>
</dl>
<h2>LINKING OPTIONS</h2>
<dl>
<dt><code>-shared</code></p>
<dd> Generate a shared library (as opposed to an executable) [dynamic] </p>
<dt><code>-fPIC</code></p>
<dd> Generate position-independent code (where available) [static] </p>
<dt><code>-dynamic</code></p>
<dd> Use dynamic Haskell libraries (if available) [static] </p>
<dt><code>-dynload</code></p>
<dd> Selects one of a number of modes for finding shared libraries at runtime. [static] </p>
<dt><code>-framework</code> <i>name</i></p>
<dd> On Darwin/MacOS X only, link in the framework <i>name</i>. This option corresponds to the <code>-framework</code> option for Apple&#8217;s Linker. [dynamic] </p>
<dt><code>-framework-path</code> <i>name</i></p>
<dd> On Darwin/MacOS X only, add <i>dir</i> to the list of directories searched for frameworks. This option corresponds to the <code>-F</code> option for Apple&#8217;s Linker. [dynamic] </p>
<dt><code>-l</code><i>lib</i></p>
<dd> Link in library <i>lib</i> [dynamic] </p>
<dt><code>-L</code><i>dir</i></p>
<dd> Add <i>dir</i> to the list of directories searched for libraries [dynamic] </p>
<dt><code>-main-is</code></p>
<dd> Set main module and function [dynamic] </p>
<dt><code>&#8211;mk-dll</code></p>
<dd> DLL-creation mode (Windows only) [dynamic] </p>
<dt><code>-no-hs-main</code></p>
<dd> Don&#8217;t assume this program contains main [dynamic] </p>
<dt><code>-rtsopts</code>, <code>-rtsopts={none,some,all}</code></p>
<dd> Control whether the RTS behaviour can be tweaked via command-line flags and the GHCRTS environment variable. Using none means no RTS flags can be given; some means only a minimum of safe options can be given (the default), and all (or no argument at all) means that all RTS flags are permitted. [dynamic] </p>
<dt><code>-with-rtsopts=opts</code></p>
<dd> Set the default RTS options to <i>opts</i>. [dynamic] </p>
<dt><code>-no-link</code></p>
<dd> Omit linking [dynamic] </p>
<dt><code>-split-objs</code></p>
<dd> Split objects (for libraries) [dynamic] </p>
<dt><code>-static</code></p>
<dd> Use static Haskell libraries [static] </p>
<dt><code>-threaded</code></p>
<dd> Use the threaded runtime [static] </p>
<dt><code>-debug</code></p>
<dd> Use the debugging runtime [static] </p>
<dt><code>-eventlog</code></p>
<dd> Enable runtime event tracing [static] </p>
<dt><code>-fno-gen-manifest</code></p>
<dd> Do not generate a manifest file (Windows only) [dynamic] </p>
<dt><code>-fno-embed-manifest</code></p>
<dd> Do not embed the manifest in the executable (Windows only) [dynamic] </p>
<dt><code>-fno-shared-implib</code></p>
<dd> Don&#8217;t generate an import library for a DLL (Windows only) [dynamic] </p>
<dt><code>-dylib-install-name</code> <i>path</i></p>
<dd> Set the install name (via -install_name passed to Apple&#8217;s linker), specifying the full install path of the library file. Any libraries or executables that link with it later will pick up that path as their runtime search location for it. (Darwin/MacOS X only) [dynamic] </p>
</dl>
<h2>PLUGIN OPTIONS</h2>
<dl>
<dt><code>-fplugin</code>=<i>module</i></p>
<dd> Load a plugin exported by a given module [static] </p>
<dt><code>-fplugin-opt</code>=<i>module:args</i></p>
<dd> Give arguments to a plugin module; module must be specified with <code>-fplugin</code> [static] </p>
</dl>
<h2>REPLACING PHASES</h2>
<dl>
<dt><code>-pgmL</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the literate pre-processor [dynamic] </p>
<dt><code>-pgmP</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the C pre-processor (with <code>-cpp</code> only) [dynamic] </p>
<dt><code>-pgmc</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the C compiler [dynamic] </p>
<dt><code>-pgms</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the splitter [dynamic] </p>
<dt><code>-pgma</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the assembler [dynamic] </p>
<dt><code>-pgml</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the linker [dynamic] </p>
<dt><code>-pgmdll</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the DLL generator [dynamic] </p>
<dt><code>-pgmF</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the pre-processor (with <code>-F</code> only) [dynamic] </p>
<dt><code>-pgmwindres</code> <i>cmd</i></p>
<dd> Use <i>cmd</i> as the program for embedding manifests on Windows. [dynamic] </p>
</dl>
<h2>FORCING OPTIONS TO PARTICULAR PHASES</h2>
<dl>
<dt><code>-optL</code> <i>option</i></p>
<dd> pass <i>option</i> to the literate pre-processor [dynamic] </p>
<dt><code>-optP</code> <i>option</i></p>
<dd> pass <i>option</i> to cpp (with <code>-cpp</code> only) [dynamic] </p>
<dt><code>-optF</code> <i>option</i></p>
<dd> pass <i>option</i> to the custom pre-processor [dynamic] </p>
<dt><code>-optc</code> <i>option</i></p>
<dd> pass <i>option</i> to the C compiler [dynamic] </p>
<dt><code>-optlo</code> <i>option</i></p>
<dd> pass <i>option</i> to the LLVM optimiser [dynamic] </p>
<dt><code>-optlc</code> <i>option</i></p>
<dd> pass <i>option</i> to the LLVM compiler [dynamic] </p>
<dt><code>-optm</code> <i>option</i></p>
<dd> pass <i>option</i> to the mangler [dynamic] </p>
<dt><code>-opta</code> <i>option</i></p>
<dd> pass <i>option</i> to the assembler [dynamic] </p>
<dt><code>-optl</code> <i>option</i></p>
<dd> pass <i>option</i> to the linker [dynamic] </p>
<dt><code>-optdll</code> <i>option</i></p>
<dd> pass <i>option</i> to the DLL generator [dynamic] </p>
<dt><code>-optwindres</code> <i>option</i></p>
<dd> pass <i>option</i> to windres. [dynamic] </p>
</dl>
<h2>PLATFORM-SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-msse2</code></p>
<dd> (x86 only) Use SSE2 for floating point [dynamic] </p>
<dt><code>-monly-[432]-regs</code></p>
<dd> (x86 only) give some registers back to the C compiler [dynamic] </p>
</dl>
<h2>EXTERNAL CORE FILE OPTIONS</h2>
<dl>
<dt><code>-fext-core</code></p>
<dd> Generate .hcr external Core files [dynamic] </p>
</dl>
<h2>COMPILER DEBUGGING OPTIONS</h2>
<dl>
<dt><code>-dcore-lint</code></p>
<dd> Turn on internal sanity checking [dynamic] </p>
<dt><code>-ddump-to-file</code></p>
<dd> Dump to files instead of stdout [dynamic] </p>
<dt><code>-ddump-asm</code></p>
<dd> Dump assembly [dynamic] </p>
<dt><code>-ddump-bcos</code></p>
<dd> Dump interpreter byte code [dynamic] </p>
<dt><code>-ddump-cmm</code></p>
<dd> Dump C&#8211; output [dynamic] </p>
<dt><code>-ddump-core-stats</code></p>
<dd> Print a one-line summary of the size of the Core program at the end of the optimisation pipeline [dynamic] </p>
<dt><code>-ddump-cpranal</code></p>
<dd> Dump output from CPR analysis [dynamic] </p>
<dt><code>-ddump-cse</code></p>
<dd> Dump CSE output [dynamic] </p>
<dt><code>-ddump-deriv</code></p>
<dd> Dump deriving output [dynamic] </p>
<dt><code>-ddump-ds</code></p>
<dd> Dump desugarer output [dynamic] </p>
<dt><code>-ddump-flatC</code></p>
<dd> Dump `flat&#8217; C [dynamic] </p>
<dt><code>-ddump-foreign</code></p>
<dd> Dump foreign export stubs [dynamic] </p>
<dt><code>-ddump-hpc</code></p>
<dd> Dump after instrumentation for program coverage [dynamic] </p>
<dt><code>-ddump-inlinings</code></p>
<dd> Dump inlining info [dynamic] </p>
<dt><code>-ddump-llvm</code></p>
<dd> Dump LLVM intermediate code [dynamic] </p>
<dt><code>-ddump-occur-anal</code></p>
<dd> Dump occurrence analysis output [dynamic] </p>
<dt><code>-ddump-opt-cmm</code></p>
<dd> Dump the results of C&#8211; to C&#8211; optimising passes [dynamic] </p>
<dt><code>-ddump-parsed</code></p>
<dd> Dump parse tree [dynamic] </p>
<dt><code>-ddump-prep</code></p>
<dd> Dump prepared core [dynamic] </p>
<dt><code>-ddump-rn</code></p>
<dd> Dump renamer output [dynamic] </p>
<dt><code>-ddump-rule-firings</code></p>
<dd> Dump rule firing info [dynamic] </p>
<dt><code>-ddump-rule-rewrites</code></p>
<dd> Dump detailed rule firing info [dynamic] </p>
<dt><code>-ddump-rules</code></p>
<dd> Dump rules [dynamic] </p>
<dt><code>-ddump-vect</code></p>
<dd> Dump vectoriser input and output [dynamic] </p>
<dt><code>-ddump-simpl</code></p>
<dd> Dump final simplifier output [dynamic] </p>
<dt><code>-ddump-simpl-phases</code></p>
<dd> Dump output from each simplifier phase [dynamic] </p>
<dt><code>-ddump-simpl-iterations</code></p>
<dd> Dump output from each simplifier iteration [dynamic] </p>
<dt><code>-ddump-spec</code></p>
<dd> Dump specialiser output [dynamic] </p>
<dt><code>-ddump-splices</code></p>
<dd> Dump TH spliced expressions, and what they evaluate to [dynamic] </p>
<dt><code>-ddump-stg</code></p>
<dd> Dump final STG [dynamic] </p>
<dt><code>-ddump-stranal</code></p>
<dd> Dump strictness analyser output [dynamic] </p>
<dt><code>-ddump-tc</code></p>
<dd> Dump typechecker output [dynamic] </p>
<dt><code>-ddump-types</code></p>
<dd> Dump type signatures [dynamic] </p>
<dt><code>-ddump-worker-wrapper</code></p>
<dd> Dump worker-wrapper output [dynamic] </p>
<dt><code>-ddump-if-trace</code></p>
<dd> Trace interface files [dynamic] </p>
<dt><code>-ddump-tc-trace</code></p>
<dd> Trace typechecker [dynamic] </p>
<dt><code>-ddump-vt-trace</code></p>
<dd> Trace vectoriser [dynamic] </p>
<dt><code>-ddump-rn-trace</code></p>
<dd> Trace renamer [dynamic] </p>
<dt><code>-ddump-rn-stats</code></p>
<dd> Renamer stats [dynamic] </p>
<dt><code>-ddump-simpl-stats</code></p>
<dd> Dump simplifier stats [dynamic] </p>
<dt><code>-dno-debug-output</code></p>
<dd> Suppress unsolicited debugging output [static] </p>
<dt><code>-dppr-debug</code></p>
<dd> Turn on debug printing (more verbose) [static] </p>
<dt><code>-dppr-noprags</code></p>
<dd> Don&#8217;t output pragma info in dumps [static] </p>
<dt><code>-dppr-user-length</code></p>
<dd> Set the depth for printing expressions in error msgs [dynamic] </p>
<dt><code>-dppr-colsNNN</code></p>
<dd> Set the width of debugging output. For example <code>-dppr-cols200</code> [dynamic] </p>
<dt><code>-dppr-case-as-let</code></p>
<dd> Print single alternative case expressions as strict lets. [dynamic] </p>
<dt><code>-dsuppress-all</code></p>
<dd> In core dumps, suppress everything that is suppressable. [static] </p>
<dt><code>-dsuppress-uniques</code></p>
<dd> Suppress the printing of uniques in debug output (easier to use diff) [static] </p>
<dt><code>-dsuppress-idinfo</code></p>
<dd> Suppress extended information about identifiers where they are bound [static] </p>
<dt><code>-dsuppress-module-prefixes</code></p>
<dd> Suppress the printing of module qualification prefixes [static] </p>
<dt><code>-dsuppress-type-signatures</code></p>
<dd> Suppress type signatures [static] </p>
<dt><code>-dsuppress-type-applications</code></p>
<dd> Suppress type applications [static] </p>
<dt><code>-dsuppress-coercions</code></p>
<dd> Suppress the printing of coercions in Core dumps to make them shorter [static] </p>
<dt><code>-dsource-stats</code></p>
<dd> Dump haskell source stats [dynamic] </p>
<dt><code>-dcmm-lint</code></p>
<dd> C&#8211; pass sanity checking [dynamic] </p>
<dt><code>-dstg-lint</code></p>
<dd> STG pass sanity checking [dynamic] </p>
<dt><code>-dstg-stats</code></p>
<dd> Dump STG stats [dynamic] </p>
<dt><code>-dverbose-core2core</code></p>
<dd> Show output from each core-to-core pass [dynamic] </p>
<dt><code>-dverbose-stg2stg</code></p>
<dd> Show output from each STG-to-STG pass [dynamic] </p>
<dt><code>-dshow-passes</code></p>
<dd> Print out each pass name as it happens [dynamic] </p>
<dt><code>-dfaststring-stats</code></p>
<dd> Show statistics for fast string usage when finished [dynamic] </p>
</dl>
<h2>MISC COMPILER OPTIONS</h2>
<dl>
<dt><code>-fno-hi-version-check</code></p>
<dd> Don&#8217;t complain about .hi file mismatches [static] </p>
<dt><code>-dno-black-holing</code></p>
<dd> Turn off black holing (probably doesn&#8217;t work) [static] </p>
<dt><code>-fhistory-size</code></p>
<dd> Set simplification history size [static] </p>
<dt><code>-funregisterised</code></p>
<dd> Unregisterised compilation (use <code>-unreg</code> instead) [static] </p>
<dt><code>-fno-ghci-history</code></p>
<dd> Do not use the load/store the GHCi command history from/to ghci_history. [dynamic] </p>
<dt><code>-fno-ghci-sandbox</code></p>
<dd> Turn off the GHCi sandbox. Means computations are run in the main thread, rather than a forked thread. [dynamic] </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/lib64</i> </p>
<h2>COPYRIGHT</h2>
<p> Copyright 2002, The University Court of the University of Glasgow.<br />
 All rights reserved. </p>
<h2>AUTHOR</h2>
<p> This manual page was generated from the XML documentation of GHC with blood, sweat, tears and a breaks-if-you-look-at-it-the-wrong-way XSL stylesheet originally written by Michael Weber &lt;michaelw [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
