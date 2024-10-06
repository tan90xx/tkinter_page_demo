#############################################################################
# Generated by PAGE version 6.1
#  in conjunction with Tcl version 8.6
#  May 10, 2021 01:18:59 PM CST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1284x701+304+151
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1284 701
    wm minsize $top 180 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "小海垃圾分类管家"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 5 -relief groove -background #f1ede6 -height 544 \
        -highlightbackground #ffffff -highlightcolor black -width 991 
    vTcl:DefineAlias "$top.fra45" "main" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    ttk::separator $site_3_0.tSe46 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe46" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.tSe46
    message $site_3_0.mes47 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 18 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #453735 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 语音识别垃圾分类系统 -width 483 
    vTcl:DefineAlias "$site_3_0.mes47" "title" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.mes47
    message $site_3_0.mes45 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #99682d -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -justify center \
        -text {请告诉小海你想投放的垃圾名称，
例如香蕉皮、啤酒瓶……} -width 473 
    vTcl:DefineAlias "$site_3_0.mes45" "message1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.mes45
    message $site_3_0.mes46 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 语言选择类型 -width 162 
    vTcl:DefineAlias "$site_3_0.mes46" "language" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.mes46
    ttk::combobox $site_3_0.tCo48 \
        -textvariable combobox -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo48" "languagechoose" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.tCo48
    button $site_3_0.but50 \
        -activebackground #000000 -activeforeground #000000 \
        -background #000000 -disabledforeground #a3a3a3 \
        -font {-family 微软雅黑 -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor #ffffff -pady 0 -text 开始识别 
    vTcl:DefineAlias "$site_3_0.but50" "begin" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.but50
    ttk::separator $site_3_0.tSe51
    vTcl:DefineAlias "$site_3_0.tSe51" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.tSe51
    button $site_3_0.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -anchor e -background #f1ede6 -borderwidth 3 -command choose \
        -disabledforeground #a3a3a3 \
        -font {-family 微软雅黑 -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #f1ede6 \
        -highlightcolor #f1ede6 -highlightthickness 0 -pady 0 \
        -text {音频选择    } 
    vTcl:DefineAlias "$site_3_0.but55" "audiochoose" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.but55
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -anchor e -background #f1ede6 -disabledforeground #a3a3a3 \
        -font {-family 微软雅黑 -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {实时录音    } 
    vTcl:DefineAlias "$site_3_0.but56" "audiorecord" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.but56
    message $site_3_0.mes57 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 8 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #a5a2a5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 声明：上传音频除作识别外无其他用途，请无需担心您的隐私泄露。 -width 484 
    vTcl:DefineAlias "$site_3_0.mes57" "statement1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.mes57
    frame $site_3_0.fra47 \
        -borderwidth 2 -relief groove -background #f1ede6 -height 705 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 784 
    vTcl:DefineAlias "$site_3_0.fra47" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra47
    message $site_4_0.mes45 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 16 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #453735 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 垃圾分类排行榜 -width 483 
    vTcl:DefineAlias "$site_4_0.mes45" "listtitle" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.mes45
    listbox $site_4_0.lis49 \
        -background #e7dfd3 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -height 546 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -selectbackground blue -selectforeground white -width 534 
    $site_4_0.lis49 configure -font "TkFixedFont"
    $site_4_0.lis49 insert end text
    vTcl:DefineAlias "$site_4_0.lis49" "Listbox1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.lis49
    place $site_4_0.mes45 \
        -in $site_4_0 -x 0 -relx 0.204 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.616 -height 0 -relheight 0.067 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lis49 \
        -in $site_4_0 -x 0 -relx 0.179 -y 0 -rely 0.099 -width 0 \
        -relwidth 0.681 -height 0 -relheight 0.774 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $site_3_0.fra47
    canvas $site_3_0.can50 \
        -background #f1ede6 -borderwidth 2 -closeenough 1.0 -height 113 \
        -highlightbackground #f1ede6 -highlightcolor #f1ede6 \
        -insertbackground #f1ede6 -relief ridge -selectbackground #f1ede6 \
        -selectforeground #f1ede6 -width 123 
    vTcl:DefineAlias "$site_3_0.can50" "folder" vTcl:WidgetProc "Toplevel1" 1
    canvas $site_3_0.can51 \
        -background #f1ede6 -borderwidth 2 -closeenough 1.0 -height 75 \
        -highlightbackground #f1ede6 -highlightcolor #646464 \
        -insertbackground #f1ede6 -relief ridge -selectbackground #00ffff \
        -selectforeground white -width 125 
    vTcl:DefineAlias "$site_3_0.can51" "microphone" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_3_0.can51
    frame $site_3_0.fra51 \
        -relief groove -background #f1ede6 -height 674 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 753 
    vTcl:DefineAlias "$site_3_0.fra51" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra51
    message $site_4_0.mes45 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 16 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #453735 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 为你分类中 -width 483 
    vTcl:DefineAlias "$site_4_0.mes45" "fenleizhong" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.mes45
    canvas $site_4_0.can52 \
        -background #ffffff -borderwidth 2 -closeenough 1.0 -height 293 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground blue \
        -selectforeground white -width 713 
    vTcl:DefineAlias "$site_4_0.can52" "process" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.can52
    text $site_4_0.tex53 \
        -background #f1ede6 -font {-family {宋体} -size 9} -foreground black \
        -height 260 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -insertbackground black -relief flat \
        -selectbackground blue -selectforeground #ffffffffffff -width 646 \
        -wrap word 
    $site_4_0.tex53 configure -font "-family {宋体} -size 9"
    $site_4_0.tex53 insert end text
    vTcl:DefineAlias "$site_4_0.tex53" "processmessage" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.tex53
    place $site_4_0.mes45 \
        -in $site_4_0 -x 0 -relx 0.205 -y 0 -rely 0.013 -width 0 \
        -relwidth 0.615 -height 0 -relheight 0.068 -anchor nw \
        -bordermode ignore 
    place $site_4_0.can52 \
        -in $site_4_0 -x 0 -relx 0.046 -y 0 -rely 0.109 -width 0 \
        -relwidth 0.913 -height 0 -relheight 0.416 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tex53 \
        -in $site_4_0 -x 0 -relx 0.09 -y 0 -rely 0.554 -width 0 \
        -relwidth 0.826 -height 0 -relheight 0.355 -anchor nw \
        -bordermode ignore 
    frame $site_3_0.fra58 \
        -relief ridge -background #f1ede6 -height 674 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 753 
    vTcl:DefineAlias "$site_3_0.fra58" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra58
    message $site_4_0.mes45 \
        -background #f1ede6 \
        -font {-family 微软雅黑 -size 16 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #453735 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 识别结果 -width 483 
    vTcl:DefineAlias "$site_4_0.mes45" "Resulttitle" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.mes45
    message $site_4_0.mes46 \
        -background #f1ede6 \
        -font {-family {Microsoft YaHei UI} -size 24 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor #000000 \
        -text ……属于可回收物 -width 194 
    vTcl:DefineAlias "$site_4_0.mes46" "result" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.mes46
    text $site_4_0.tex47 \
        -background #eedcc6 -font TkTextFont -foreground black -height 313 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 294 -wrap word 
    $site_4_0.tex47 configure -font "TkTextFont"
    $site_4_0.tex47 insert end text
    vTcl:DefineAlias "$site_4_0.tex47" "introduction" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.tex47
    canvas $site_4_0.can48 \
        -background #f1ede6 -borderwidth 2 -closeenough 1.0 \
        -cursor bottom_side -height 412 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground #f1ede6 -relief ridge -selectbackground blue \
        -selectforeground #f1ede6 -width 373 
    vTcl:DefineAlias "$site_4_0.can48" "trashcan" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.can48
    ttk::separator $site_4_0.tSe50
    vTcl:DefineAlias "$site_4_0.tSe50" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.tSe50
    message $site_4_0.mes52 \
        -anchor w -background #f1ede6 \
        -font {-family 微软雅黑 -size 8 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #a5a2a5 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text 相关内容由人工智能技术生成。 -width 436 
    vTcl:DefineAlias "$site_4_0.mes52" "statement2" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.mes52
    text $site_4_0.tex53 \
        -background #f1ede6 -font TkTextFont -foreground black -height 114 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 333 -wrap word 
    $site_4_0.tex53 configure -font "TkTextFont"
    $site_4_0.tex53 insert end text
    vTcl:DefineAlias "$site_4_0.tex53" "search" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.tex53
    place $site_4_0.mes45 \
        -in $site_4_0 -x 0 -relx 0.205 -y 0 -rely 0.013 -width 0 \
        -relwidth 0.615 -height 0 -relheight 0.068 -anchor nw \
        -bordermode ignore 
    place $site_4_0.mes46 \
        -in $site_4_0 -x 0 -relx 0.463 -y 0 -rely 0.076 -width 0 \
        -relwidth 0.261 -height 0 -relheight 0.228 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tex47 \
        -in $site_4_0 -x 0 -relx 0.592 -y 0 -rely 0.295 -width 0 \
        -relwidth 0.396 -height 0 -relheight 0.445 -anchor nw \
        -bordermode ignore 
    place $site_4_0.can48 \
        -in $site_4_0 -x 0 -relx 0.013 -y 0 -rely 0.281 -width 0 \
        -relwidth 0.502 -height 0 -relheight 0.609 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tSe50 \
        -in $site_4_0 -x 0 -relx 0.013 -y 0 -rely 0.947 -width 0 \
        -relwidth 0.511 -height 0 -relheight 0.004 -anchor nw \
        -bordermode inside 
    place $site_4_0.mes52 \
        -in $site_4_0 -x 0 -relx 0.013 -y 0 -rely 0.963 -width 0 \
        -relwidth 0.587 -height 0 -relheight 0.036 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tex53 \
        -in $site_4_0 -x 0 -relx 0.538 -y 0 -rely 0.795 -width 0 \
        -relwidth 0.448 -height 0 -relheight 0.162 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $site_3_0.fra58
    place $site_3_0.tSe46 \
        -in $site_3_0 -x 0 -relx 0.39 -y 0 -width 0 -relwidth 0.002 -height 0 \
        -relheight 0.994 -anchor nw -bordermode inside 
    place $site_3_0.mes47 \
        -in $site_3_0 -x 0 -relx 0.008 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.376 -height 0 -relheight 0.066 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes45 \
        -in $site_3_0 -x 0 -relx 0.016 -y 0 -rely 0.099 -width 0 \
        -relwidth 0.367 -height 0 -relheight 0.085 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes46 \
        -in $site_3_0 -x 0 -relx 0.039 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo48 \
        -in $site_3_0 -x 0 -relx 0.187 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.144 -height 0 -relheight 0.042 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 0 -relx 0.132 -y 0 -rely 0.762 -width 159 \
        -relwidth 0 -height 71 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe51 \
        -in $site_3_0 -x 0 -relx 0.014 -y 0 -rely 0.923 -width 0 \
        -relwidth 0.355 -height 0 -relheight 0.004 -anchor nw \
        -bordermode inside 
    place $site_3_0.but55 \
        -in $site_3_0 -x 0 -relx 0.078 -y 0 -rely 0.296 -width 309 \
        -relwidth 0 -height 115 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.078 -y 0 -rely 0.536 -width 309 \
        -relwidth 0 -height 115 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes57 \
        -in $site_3_0 -x 0 -relx 0.007 -y 0 -rely 0.922 -width 0 \
        -relwidth 0.377 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra47 \
        -in $site_3_0 -x 0 -relx 0.405 -y 0 -rely 0.028 -width 0 \
        -relwidth 0.578 -height 0 -relheight 0.952 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can50 \
        -in $site_3_0 -x 0 -relx 0.086 -y 0 -rely 0.296 -width 0 \
        -relwidth 0.096 -height 0 -relheight 0.159 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can51 \
        -in $site_3_0 -x 0 -relx 0.086 -y 0 -rely 0.536 -width 0 \
        -relwidth 0.096 -height 0 -relheight 0.159 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra51 \
        -in $site_3_0 -x 0 -relx 0.405 -y 0 -rely 0.028 -width 0 \
        -relwidth 0.578 -height 0 -relheight 0.952 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra58 \
        -in $site_3_0 -x 0 -relx 0.405 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.578 -height 0 -relheight 0.952 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra45
    menu $top.m45 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.001 -height 0 \
        -relheight 1.011 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

