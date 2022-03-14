from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
KV='''
#:import Clipboard kivy.core.clipboard.Clipboard
Manager:
    Menu:
    RGB:
    VIBGYR:
    Blender:
    Gradient:
    lang:
    lang_2:
    lang_3:
    lang_4:
    Theory:
    About:
<Menu>:
    name: 'Menu'
    id:Menu
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1,.122
            Label:
                text: "|| Color Picker ||"
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'header.png'
        BoxLayout:
            spacing: '15dp'
            padding:("15dp", "15dp", "15dp", "15dp")
            orientation:"vertical"
            canvas.before:
                Rectangle:
                    size:self.size
                    pos:self.pos
                    source:'mainbg.png'
            BoxLayout:
                spacing: "15dp"
                Button:
                    text:"RGB Picker"
                    background_normal:'2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'RGB'
                Button:
                    text:"VIBGYR Picker"
                    background_normal: '2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'VIBGYR'
            BoxLayout:
                spacing: "15dp"
                Button:
                    text:"Blend Color"
                    background_normal: '2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'Blender'
                Button:
                    text:"Pick Gradient"
                    background_normal: '2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'Gradient'
        BoxLayout:
            size_hint:1,.122
            orientation:"vertical"
            Label:
                text: "|| Documentation ||"
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'header.png'
        BoxLayout:
            size_hint:1,.5
            spacing: '15dp'
            padding:("15dp", "15dp", "15dp", "15dp")
            orientation:"vertical"
            canvas.before:
                Rectangle:
                    size:self.size
                    pos:self.pos
                    source:'mainbg.png'
            BoxLayout:
                spacing: "15dp"
                Button:
                    text:"Theory"
                    background_normal: '2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'Theory'
                Button:
                    text:"About"
                    background_normal: '2.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'About'
<RGB>:
    name: 'RGB'
    id:RGB
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation:"vertical"
        BoxLayout:
            orientation:"horizontal"
            size_hint: 1,.2
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'RGB'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        # Dont remove this BoxLayout, canvas wont work
        BoxLayout:
            orientation:"vertical"
            size_hint:1, .4
            padding:("0dp","15dp","0dp","15dp")
            BoxLayout:
                orientation:"vertical"
                size_hint:1, None
                height: "0dp"
                Label:
                    text:""
                    background_color:(0,1,0,0)
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
            Slider:
                id:main_slider
                min:0
                max:60
                value:32
                size_hint:1, 1
                orientation:"horizontal"
                canvas.before:
                    Rectangle:
                        pos: self.x + 20, self.y
                        size: (self.width - 40 ), self.height
                        source:'cp_main.png'
        BoxLayout:
            orientation:"horizontal"
            padding:("15dp","0dp","15dp","0dp")
            size_hint: 1, .25
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  5  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  5  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  5  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  15  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  15  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  15  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  25  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  25  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  25  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  35  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  35  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  35  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  45  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  45  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  45  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  55  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  55  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  55  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  65  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  65  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  65  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  75  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  75  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  75  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  85  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  85  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  85  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  95  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  95  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  95  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  105  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  105  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  105  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  115  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  115  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  115  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  125  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  125  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  125  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  135  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  135  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  135  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  145  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  145  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  145  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  155  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  155  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  155  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  165  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  165  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  165  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  175  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  175  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  175  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  185  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  185  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  185  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  195  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  195  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  195  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
            Label:
                text:""
                size_hint:1, 1
                background_color:(float(  (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (  205  )))  ), float(  (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (  205  )))  ), float(  (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (  205  )))  ), int(1))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
        Slider:
            id:re_slider
            min:0
            max:209
            value:105
            size_hint:1, .25
            orientation:"horizontal"
        BoxLayout:
            padding:("15dp","0dp","15dp","0dp")
            size_hint:1,.25
            Label:
                id:main_preview
                text:""
                size_hint:1, 1
                background_color:float((RGB_R.value)/100), float((RGB_G.value)/100), float((RGB_B.value)/100), root.transperancy(switch1.active, float((RGB_T.value)/100))
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
        BoxLayout:
            padding:('15dp','15dp','0dp','0dp')
            orientation:"vertical"
            BoxLayout:
                orientation:"horizontal"
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:RGB_R
                    min:0
                    max:100
                    value:100 * (root.re_processor(((root.main_processor("red", int(main_slider.value)))), (int(re_slider.value))))
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation:"horizontal"
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:RGB_G
                    min:0
                    max:100
                    value:100 * (root.re_processor(((root.main_processor("green", int(main_slider.value)))), (int(re_slider.value))))
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation:"horizontal"
                Label:
                    text:'Blue'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:RGB_B
                    min:0
                    max:100
                    value:100 * (root.re_processor(((root.main_processor("blue", int(main_slider.value)))), (int(re_slider.value))))
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation:"horizontal"
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    size_hint:.3,1
                    font_size: "12dp"
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:RGB_T
                    min:0
                    max:100
                    value:100
                    size_hint:1,1
                    orientation:"horizontal"
                    disabled: not switch1.active
        BoxLayout:
            size_hint: 1, .20
            orientation: "horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Transparency"
                Switch:
                    id: switch1
                    active: True
            BoxLayout:
                size_hint: .5, 1
                padding:("15dp","7.5dp","15dp","7.5dp")
                Button:
                    id: lang_select
                    text: root.color_value
                    halign: "center"
                    background_normal: '3.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'lang'
        BoxLayout:
            orientation:"vertical"
            size_hint:1, .125
            Label:
                text:"Click to Copy Convenient Value"
                color:1,1,1,.7
        BoxLayout:
            orientation: "vertical"
            size_hint: 1, .20
            BoxLayout:
                orientation: "vertical"
                BoxLayout:
                    orientation:"vertical"
                    Button:
                        id:color_main
                        text:root.all_type(int(RGB_R.value), int(RGB_G.value), int(RGB_B.value), int(RGB_T.value), switch1.active, root.color_value)
                        size_hint:1, 1
                        background_normal: '5.png'
                        on_release:
                            Clipboard.copy(self.text)
<VIBGYR>:
    name: 'VIBGYR'
    id:VIBGYR
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation:"vertical"
        BoxLayout:
            orientation:"horizontal"
            size_hint: 1,.125
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'VIBGYR'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        BoxLayout:
            size_hint:1,.3
            padding:("15dp","15dp","15dp","15dp")
            Label:
                text:""
                background_color: root.VIBGYR_preview(VIBGYR_V.value,VIBGYR_I.value,VIBGYR_B.value,VIBGYR_G.value,VIBGYR_Y.value,VIBGYR_R.value,VIBGYR_T.value,switch2.active)
                canvas.before:
                    Color:
                        rgba:self.background_color
                    Rectangle:
                        size:self.size
                        pos:self.pos
        BoxLayout:
            padding:("15dp","0dp","0dp","0dp")
            orientation: "vertical"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Violet"
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'v.png'
                Slider:
                    id:VIBGYR_V
                    min:0
                    max:100
                    value:0
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:'Indigo'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:VIBGYR_I
                    min:0
                    max:100
                    value:100
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Blue"
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'cyan.png'
                Slider:
                    id:VIBGYR_B
                    min:0
                    max:100
                    value:100
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:VIBGYR_G
                    min:0
                    max:100
                    value:100
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Yellow"
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'y.png'
                Slider:
                    id:VIBGYR_Y
                    min:0
                    max:100
                    value:0
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:VIBGYR_R
                    min:0
                    max:100
                    value:0
                    size_hint:1,1
                    orientation:"horizontal"
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    size_hint:.3,1
                    font_size: "12dp"
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:VIBGYR_T
                    min:0
                    max:100
                    value:100
                    size_hint:1,1
                    orientation:"horizontal"
                    disabled: not switch2.active
        BoxLayout:
            size_hint: 1, .15
            orientation: "horizontal"
            padding:("0dp","0dp","0dp","0dp")
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Transparency"
                Switch:
                    id: switch2
                    active: True
            BoxLayout:
                size_hint: .5, 1
                padding:("15dp","10dp","15dp","10dp")
                Button:
                    id: lang_select
                    text: root.color_value
                    halign: "center"
                    background_normal: '3.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'lang_2'
        BoxLayout:
            orientation:"vertical"
            size_hint:1, .08
            Label:
                text:"Click to Copy Convenient Value"
                color:1,1,1,.7
        BoxLayout:
            size_hint: 1,.125
            Button:
                text: root.VIBGYR(VIBGYR_V.value,VIBGYR_I.value,VIBGYR_B.value,VIBGYR_G.value,VIBGYR_Y.value,VIBGYR_R.value,VIBGYR_T.value,switch2.active,root.color_value)
                size_hint:1, 1
                background_normal: '5.png'
                on_release:
                    Clipboard.copy(self.text)
<Blender>:
    name:"Blender"
    id:Blender
    BoxLayout:
        orientation:"vertical"
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        BoxLayout:
            size_hint:1,.25
            orientation:"horizontal"
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'Blender'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Color 1 :'
                font_size: "12dp"
            Label:
                text:root.show_color_single(R_1.value,G_1.value,B_1.value,T_1.value,switch3.active,root.color_value)
                font_size: "12dp"
            BoxLayout:
                padding:('15dp','7.5dp','15dp','7.5dp')
                Label:
                    text:""
                    background_color:(float(float(R_1.value)/100), float(float(G_1.value)/100), float(float(B_1.value)/100), root.transperancy(switch3.active, float(float(T_1.value)/100)))
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:R_1
                    min:0
                    max:100
                    value:0
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:G_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Blue'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:B_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    size_hint:.3,1
                    font_size: "12dp"
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:T_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
                    disabled:not switch3.active
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Color 2 :'
                font_size: "12dp"
            Label:
                text:root.show_color_single(R_2.value,G_2.value,B_2.value,T_2.value,switch3.active,root.color_value)
                font_size: "12dp"
            BoxLayout:
                padding:('15dp','7.5dp','15dp','7.5dp')
                Label:
                    text:""
                    background_color:(float(float(R_2.value)/100), float(float(G_2.value)/100), float(float(B_2.value)/100), root.transperancy(switch3.active, float(float(T_2.value)/100)))
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:R_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:G_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Blue'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:B_2
                    min:0
                    max:100
                    value:0
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    font_size: "12dp"
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:T_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
                    disabled:not switch3.active
        BoxLayout:
            size_hint:1,.25
            orientation: "horizontal"
            padding:("0dp","0dp","0dp","0dp")
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Transparency"
                Switch:
                    id: switch3
                    active: True
            BoxLayout:
                size_hint: .5, 1
                padding:("15dp","7.5dp","15dp","7.5dp")
                Button:
                    id: lang_select
                    text: root.color_value
                    halign: "center"
                    background_normal: '3.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'lang_3'
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Result'
                size_hint:.3,1
            BoxLayout:
                padding:('0dp','7.5dp','15dp','0dp')
                Label:
                    text:""
                    background_color:(float(float((R_1.value + R_2.value)/2)/100), float(float((G_1.value + G_2.value)/2)/100), float(float((B_1.value + B_2.value)/2)/100), root.transperancy(switch3.active, float(float((T_1.value + T_2.value)/2)/100)))
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            size_hint:1,.2
            Label:
                text:"Click to Copy Convenient Value"
                color:1,1,1,.7
        BoxLayout:
            size_hint:1,.25
            Button:
                id:main_preview_blend
                text:root.show_color_result(R_1.value,G_1.value,B_1.value,T_1.value,R_2.value,G_2.value,B_2.value,T_2.value,switch3.active,root.color_value)
                background_normal:'5.png'
                on_release: Clipboard.copy(self.text)
<Gradient>:
    name: 'Gradient'
    id:Gradient
    BoxLayout:
        orientation:"vertical"
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        BoxLayout:
            size_hint:1,.25
            orientation:"horizontal"
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'Gradient'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Color 1 :'
                font_size: "12dp"
            Label:
                text:root.show_color_single(R_1.value,G_1.value,B_1.value,T_1.value,switch3.active,root.color_value)
                font_size: "12dp"
            BoxLayout:
                padding:('15dp','7.5dp','15dp','7.5dp')
                Label:
                    text:""
                    background_color:(float(float(R_1.value)/100), float(float(G_1.value)/100), float(float(B_1.value)/100), root.transperancy(switch3.active, float(float(T_1.value)/100)))
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:R_1
                    min:0
                    max:100
                    value:0
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:G_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Blue'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:B_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    size_hint:.3,1
                    font_size: "12dp"
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:T_1
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
                    disabled:not switch3.active
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Color 2 :'
                font_size: "12dp"
            Label:
                text:root.show_color_single(R_2.value,G_2.value,B_2.value,T_2.value,switch3.active,root.color_value)
                font_size: "12dp"
            BoxLayout:
                padding:('15dp','7.5dp','15dp','7.5dp')
                Label:
                    text:""
                    background_color:(float(float(R_2.value)/100), float(float(G_2.value)/100), float(float(B_2.value)/100), root.transperancy(switch3.active, float(float(T_2.value)/100)))
                    canvas.before:
                        Color:
                            rgba:self.background_color
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Red'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'r.png'
                Slider:
                    id:R_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Green'
                    color:0,0,0,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'g.png'
                Slider:
                    id:G_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Blue'
                    color:1,1,1,1
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'b.png'
                Slider:
                    id:B_2
                    min:0
                    max:100
                    value:0
                    step:(1)
                    orientation:'horizontal'
            BoxLayout:
                Label:
                    text:'Transparent'
                    color:0,0,0,1
                    font_size: "12dp"
                    size_hint:.3,1
                    canvas.before:
                        Rectangle:
                            size:self.size
                            pos:self.pos
                            source:'t.png'
                Slider:
                    id:T_2
                    min:0
                    max:100
                    value:100
                    step:(1)
                    orientation:'horizontal'
                    disabled:not switch3.active
        BoxLayout:
            size_hint:1,.25
            orientation: "horizontal"
            padding:("0dp","0dp","0dp","0dp")
            BoxLayout:
                orientation: "horizontal"
                Label:
                    text:"Transparency"
                Switch:
                    id: switch3
                    active: True
            BoxLayout:
                size_hint: .5, 1
                padding:("15dp","7.5dp","15dp","7.5dp")
                Button:
                    id: lang_select
                    text: root.color_value
                    halign: "center"
                    background_normal: '3.png'
                    on_release:
                        root.manager.transition.direction = 'left'
                        app.root.current = 'lang_4'
        BoxLayout:
            size_hint:1,.25
            orientation:'horizontal'
            Label:
                text:'Result'
                size_hint:.3,1
            BoxLayout:
                padding:('0dp','7.5dp','15dp','0dp')
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,0),root.show_gradient(G_1.value,G_2.value,0),root.show_gradient(B_1.value,B_2.value,0),root.show_gradient(T_1.value,T_2.value,0)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,.5),root.show_gradient(G_1.value,G_2.value,.5),root.show_gradient(B_1.value,B_2.value,.5),root.show_gradient(T_1.value,T_2.value,.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,1),root.show_gradient(G_1.value,G_2.value,1),root.show_gradient(B_1.value,B_2.value,1),root.show_gradient(T_1.value,T_2.value,1)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,1.5),root.show_gradient(G_1.value,G_2.value,1.5),root.show_gradient(B_1.value,B_2.value,1.5),root.show_gradient(T_1.value,T_2.value,1.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,2),root.show_gradient(G_1.value,G_2.value,2),root.show_gradient(B_1.value,B_2.value,2),root.show_gradient(T_1.value,T_2.value,2)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,2.5),root.show_gradient(G_1.value,G_2.value,2.5),root.show_gradient(B_1.value,B_2.value,2.5),root.show_gradient(T_1.value,T_2.value,2.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,3),root.show_gradient(G_1.value,G_2.value,3),root.show_gradient(B_1.value,B_2.value,3),root.show_gradient(T_1.value,T_2.value,3)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,3.5),root.show_gradient(G_1.value,G_2.value,3.5),root.show_gradient(B_1.value,B_2.value,3.5),root.show_gradient(T_1.value,T_2.value,3.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,4),root.show_gradient(G_1.value,G_2.value,4),root.show_gradient(B_1.value,B_2.value,4),root.show_gradient(T_1.value,T_2.value,4)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,4.5),root.show_gradient(G_1.value,G_2.value,4.5),root.show_gradient(B_1.value,B_2.value,4.5),root.show_gradient(T_1.value,T_2.value,4.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,5),root.show_gradient(G_1.value,G_2.value,5),root.show_gradient(B_1.value,B_2.value,5),root.show_gradient(T_1.value,T_2.value,5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,5.5),root.show_gradient(G_1.value,G_2.value,5.5),root.show_gradient(B_1.value,B_2.value,5.5),root.show_gradient(T_1.value,T_2.value,5.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,6),root.show_gradient(G_1.value,G_2.value,6),root.show_gradient(B_1.value,B_2.value,6),root.show_gradient(T_1.value,T_2.value,6)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,6.5),root.show_gradient(G_1.value,G_2.value,6.5),root.show_gradient(B_1.value,B_2.value,6.5),root.show_gradient(T_1.value,T_2.value,6.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,7),root.show_gradient(G_1.value,G_2.value,7),root.show_gradient(B_1.value,B_2.value,7),root.show_gradient(T_1.value,T_2.value,7)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,7.5),root.show_gradient(G_1.value,G_2.value,7.5),root.show_gradient(B_1.value,B_2.value,7.5),root.show_gradient(T_1.value,T_2.value,7.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,8),root.show_gradient(G_1.value,G_2.value,8),root.show_gradient(B_1.value,B_2.value,8),root.show_gradient(T_1.value,T_2.value,8)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,8.5),root.show_gradient(G_1.value,G_2.value,8.5),root.show_gradient(B_1.value,B_2.value,8.5),root.show_gradient(T_1.value,T_2.value,8.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,9),root.show_gradient(G_1.value,G_2.value,9),root.show_gradient(B_1.value,B_2.value,9),root.show_gradient(T_1.value,T_2.value,9)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,9.5),root.show_gradient(G_1.value,G_2.value,9.5),root.show_gradient(B_1.value,B_2.value,9.5),root.show_gradient(T_1.value,T_2.value,9.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,10),root.show_gradient(G_1.value,G_2.value,10),root.show_gradient(B_1.value,B_2.value,10),root.show_gradient(T_1.value,T_2.value,10)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,10.5),root.show_gradient(G_1.value,G_2.value,10.5),root.show_gradient(B_1.value,B_2.value,10.5),root.show_gradient(T_1.value,T_2.value,10.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,11),root.show_gradient(G_1.value,G_2.value,11),root.show_gradient(B_1.value,B_2.value,11),root.show_gradient(T_1.value,T_2.value,11)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,11.5),root.show_gradient(G_1.value,G_2.value,11.5),root.show_gradient(B_1.value,B_2.value,11.5),root.show_gradient(T_1.value,T_2.value,11.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,12),root.show_gradient(G_1.value,G_2.value,12),root.show_gradient(B_1.value,B_2.value,12),root.show_gradient(T_1.value,T_2.value,12)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,12.5),root.show_gradient(G_1.value,G_2.value,12.5),root.show_gradient(B_1.value,B_2.value,12.5),root.show_gradient(T_1.value,T_2.value,12.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,13),root.show_gradient(G_1.value,G_2.value,13),root.show_gradient(B_1.value,B_2.value,13),root.show_gradient(T_1.value,T_2.value,13)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,13.5),root.show_gradient(G_1.value,G_2.value,13.5),root.show_gradient(B_1.value,B_2.value,13.5),root.show_gradient(T_1.value,T_2.value,13.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,14),root.show_gradient(G_1.value,G_2.value,14),root.show_gradient(B_1.value,B_2.value,14),root.show_gradient(T_1.value,T_2.value,14)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,14.5),root.show_gradient(G_1.value,G_2.value,14.5),root.show_gradient(B_1.value,B_2.value,14.5),root.show_gradient(T_1.value,T_2.value,14.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,15),root.show_gradient(G_1.value,G_2.value,15),root.show_gradient(B_1.value,B_2.value,15),root.show_gradient(T_1.value,T_2.value,15)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,15.5),root.show_gradient(G_1.value,G_2.value,15.5),root.show_gradient(B_1.value,B_2.value,15.5),root.show_gradient(T_1.value,T_2.value,15.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,16),root.show_gradient(G_1.value,G_2.value,16),root.show_gradient(B_1.value,B_2.value,16),root.show_gradient(T_1.value,T_2.value,16)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,16.5),root.show_gradient(G_1.value,G_2.value,16.5),root.show_gradient(B_1.value,B_2.value,16.5),root.show_gradient(T_1.value,T_2.value,16.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,17),root.show_gradient(G_1.value,G_2.value,17),root.show_gradient(B_1.value,B_2.value,17),root.show_gradient(T_1.value,T_2.value,17)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,17.5),root.show_gradient(G_1.value,G_2.value,17.5),root.show_gradient(B_1.value,B_2.value,17.5),root.show_gradient(T_1.value,T_2.value,17.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,18),root.show_gradient(G_1.value,G_2.value,18),root.show_gradient(B_1.value,B_2.value,18),root.show_gradient(T_1.value,T_2.value,18)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,18.5),root.show_gradient(G_1.value,G_2.value,18.5),root.show_gradient(B_1.value,B_2.value,18.5),root.show_gradient(T_1.value,T_2.value,18.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,19),root.show_gradient(G_1.value,G_2.value,19),root.show_gradient(B_1.value,B_2.value,19),root.show_gradient(T_1.value,T_2.value,19)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,19.5),root.show_gradient(G_1.value,G_2.value,19.5),root.show_gradient(B_1.value,B_2.value,19.5),root.show_gradient(T_1.value,T_2.value,19.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,20),root.show_gradient(G_1.value,G_2.value,20),root.show_gradient(B_1.value,B_2.value,20),root.show_gradient(T_1.value,T_2.value,20)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,20.5),root.show_gradient(G_1.value,G_2.value,20.5),root.show_gradient(B_1.value,B_2.value,20.5),root.show_gradient(T_1.value,T_2.value,20.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,21),root.show_gradient(G_1.value,G_2.value,21),root.show_gradient(B_1.value,B_2.value,21),root.show_gradient(T_1.value,T_2.value,21)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,21.5),root.show_gradient(G_1.value,G_2.value,21.5),root.show_gradient(B_1.value,B_2.value,21.5),root.show_gradient(T_1.value,T_2.value,21.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,22),root.show_gradient(G_1.value,G_2.value,22),root.show_gradient(B_1.value,B_2.value,22),root.show_gradient(T_1.value,T_2.value,22)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,22.5),root.show_gradient(G_1.value,G_2.value,22.5),root.show_gradient(B_1.value,B_2.value,22.5),root.show_gradient(T_1.value,T_2.value,22.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,23),root.show_gradient(G_1.value,G_2.value,23),root.show_gradient(B_1.value,B_2.value,23),root.show_gradient(T_1.value,T_2.value,23)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,23.5),root.show_gradient(G_1.value,G_2.value,23.5),root.show_gradient(B_1.value,B_2.value,23.5),root.show_gradient(T_1.value,T_2.value,23.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,24),root.show_gradient(G_1.value,G_2.value,24),root.show_gradient(B_1.value,B_2.value,24),root.show_gradient(T_1.value,T_2.value,24)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,24.5),root.show_gradient(G_1.value,G_2.value,24.5),root.show_gradient(B_1.value,B_2.value,24.5),root.show_gradient(T_1.value,T_2.value,24.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,25),root.show_gradient(G_1.value,G_2.value,25),root.show_gradient(B_1.value,B_2.value,25),root.show_gradient(T_1.value,T_2.value,25)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,25.5),root.show_gradient(G_1.value,G_2.value,25.5),root.show_gradient(B_1.value,B_2.value,25.5),root.show_gradient(T_1.value,T_2.value,25.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,26),root.show_gradient(G_1.value,G_2.value,26),root.show_gradient(B_1.value,B_2.value,26),root.show_gradient(T_1.value,T_2.value,26)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,26.5),root.show_gradient(G_1.value,G_2.value,26.5),root.show_gradient(B_1.value,B_2.value,26.5),root.show_gradient(T_1.value,T_2.value,26.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,27),root.show_gradient(G_1.value,G_2.value,27),root.show_gradient(B_1.value,B_2.value,27),root.show_gradient(T_1.value,T_2.value,27)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,27.5),root.show_gradient(G_1.value,G_2.value,27.5),root.show_gradient(B_1.value,B_2.value,27.5),root.show_gradient(T_1.value,T_2.value,27.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,28),root.show_gradient(G_1.value,G_2.value,28),root.show_gradient(B_1.value,B_2.value,28),root.show_gradient(T_1.value,T_2.value,28)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,28.5),root.show_gradient(G_1.value,G_2.value,28.5),root.show_gradient(B_1.value,B_2.value,28.5),root.show_gradient(T_1.value,T_2.value,28.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,29),root.show_gradient(G_1.value,G_2.value,29),root.show_gradient(B_1.value,B_2.value,29),root.show_gradient(T_1.value,T_2.value,29)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,29.5),root.show_gradient(G_1.value,G_2.value,29.5),root.show_gradient(B_1.value,B_2.value,29.5),root.show_gradient(T_1.value,T_2.value,29.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,30),root.show_gradient(G_1.value,G_2.value,30),root.show_gradient(B_1.value,B_2.value,30),root.show_gradient(T_1.value,T_2.value,30)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,30.5),root.show_gradient(G_1.value,G_2.value,30.5),root.show_gradient(B_1.value,B_2.value,30.5),root.show_gradient(T_1.value,T_2.value,30.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,31),root.show_gradient(G_1.value,G_2.value,31),root.show_gradient(B_1.value,B_2.value,31),root.show_gradient(T_1.value,T_2.value,31)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,31.5),root.show_gradient(G_1.value,G_2.value,31.5),root.show_gradient(B_1.value,B_2.value,31.5),root.show_gradient(T_1.value,T_2.value,31.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,32),root.show_gradient(G_1.value,G_2.value,32),root.show_gradient(B_1.value,B_2.value,32),root.show_gradient(T_1.value,T_2.value,32)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,32.5),root.show_gradient(G_1.value,G_2.value,32.5),root.show_gradient(B_1.value,B_2.value,32.5),root.show_gradient(T_1.value,T_2.value,32.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,33),root.show_gradient(G_1.value,G_2.value,33),root.show_gradient(B_1.value,B_2.value,33),root.show_gradient(T_1.value,T_2.value,33)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,33.5),root.show_gradient(G_1.value,G_2.value,33.5),root.show_gradient(B_1.value,B_2.value,33.5),root.show_gradient(T_1.value,T_2.value,33.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,34),root.show_gradient(G_1.value,G_2.value,34),root.show_gradient(B_1.value,B_2.value,34),root.show_gradient(T_1.value,T_2.value,34)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,34.5),root.show_gradient(G_1.value,G_2.value,34.5),root.show_gradient(B_1.value,B_2.value,34.5),root.show_gradient(T_1.value,T_2.value,34.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,35),root.show_gradient(G_1.value,G_2.value,35),root.show_gradient(B_1.value,B_2.value,35),root.show_gradient(T_1.value,T_2.value,35)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,35.5),root.show_gradient(G_1.value,G_2.value,35.5),root.show_gradient(B_1.value,B_2.value,35.5),root.show_gradient(T_1.value,T_2.value,35.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,36),root.show_gradient(G_1.value,G_2.value,36),root.show_gradient(B_1.value,B_2.value,36),root.show_gradient(T_1.value,T_2.value,36)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,36.5),root.show_gradient(G_1.value,G_2.value,36.5),root.show_gradient(B_1.value,B_2.value,36.5),root.show_gradient(T_1.value,T_2.value,36.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,37),root.show_gradient(G_1.value,G_2.value,37),root.show_gradient(B_1.value,B_2.value,37),root.show_gradient(T_1.value,T_2.value,37)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,37.5),root.show_gradient(G_1.value,G_2.value,37.5),root.show_gradient(B_1.value,B_2.value,37.5),root.show_gradient(T_1.value,T_2.value,37.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,38),root.show_gradient(G_1.value,G_2.value,38),root.show_gradient(B_1.value,B_2.value,38),root.show_gradient(T_1.value,T_2.value,38)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,38.5),root.show_gradient(G_1.value,G_2.value,38.5),root.show_gradient(B_1.value,B_2.value,38.5),root.show_gradient(T_1.value,T_2.value,38.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,39),root.show_gradient(G_1.value,G_2.value,39),root.show_gradient(B_1.value,B_2.value,39),root.show_gradient(T_1.value,T_2.value,39)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,39.5),root.show_gradient(G_1.value,G_2.value,39.5),root.show_gradient(B_1.value,B_2.value,39.5),root.show_gradient(T_1.value,T_2.value,39.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,40),root.show_gradient(G_1.value,G_2.value,40),root.show_gradient(B_1.value,B_2.value,40),root.show_gradient(T_1.value,T_2.value,40)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,40.5),root.show_gradient(G_1.value,G_2.value,40.5),root.show_gradient(B_1.value,B_2.value,40.5),root.show_gradient(T_1.value,T_2.value,40.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,41),root.show_gradient(G_1.value,G_2.value,41),root.show_gradient(B_1.value,B_2.value,41),root.show_gradient(T_1.value,T_2.value,41)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,41.5),root.show_gradient(G_1.value,G_2.value,41.5),root.show_gradient(B_1.value,B_2.value,41.5),root.show_gradient(T_1.value,T_2.value,41.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,42),root.show_gradient(G_1.value,G_2.value,42),root.show_gradient(B_1.value,B_2.value,42),root.show_gradient(T_1.value,T_2.value,42)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,42.5),root.show_gradient(G_1.value,G_2.value,42.5),root.show_gradient(B_1.value,B_2.value,42.5),root.show_gradient(T_1.value,T_2.value,42.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,43),root.show_gradient(G_1.value,G_2.value,43),root.show_gradient(B_1.value,B_2.value,43),root.show_gradient(T_1.value,T_2.value,43)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,43.5),root.show_gradient(G_1.value,G_2.value,43.5),root.show_gradient(B_1.value,B_2.value,43.5),root.show_gradient(T_1.value,T_2.value,43.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,44),root.show_gradient(G_1.value,G_2.value,44),root.show_gradient(B_1.value,B_2.value,44),root.show_gradient(T_1.value,T_2.value,44)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,44.5),root.show_gradient(G_1.value,G_2.value,44.5),root.show_gradient(B_1.value,B_2.value,44.5),root.show_gradient(T_1.value,T_2.value,44.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,45),root.show_gradient(G_1.value,G_2.value,45),root.show_gradient(B_1.value,B_2.value,45),root.show_gradient(T_1.value,T_2.value,45)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,45.5),root.show_gradient(G_1.value,G_2.value,45.5),root.show_gradient(B_1.value,B_2.value,45.5),root.show_gradient(T_1.value,T_2.value,45.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,46),root.show_gradient(G_1.value,G_2.value,46),root.show_gradient(B_1.value,B_2.value,46),root.show_gradient(T_1.value,T_2.value,46)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,46.5),root.show_gradient(G_1.value,G_2.value,46.5),root.show_gradient(B_1.value,B_2.value,46.5),root.show_gradient(T_1.value,T_2.value,46.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,47),root.show_gradient(G_1.value,G_2.value,47),root.show_gradient(B_1.value,B_2.value,47),root.show_gradient(T_1.value,T_2.value,47)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,47.5),root.show_gradient(G_1.value,G_2.value,47.5),root.show_gradient(B_1.value,B_2.value,47.5),root.show_gradient(T_1.value,T_2.value,47.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,48),root.show_gradient(G_1.value,G_2.value,48),root.show_gradient(B_1.value,B_2.value,48),root.show_gradient(T_1.value,T_2.value,48)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,48.5),root.show_gradient(G_1.value,G_2.value,48.5),root.show_gradient(B_1.value,B_2.value,48.5),root.show_gradient(T_1.value,T_2.value,48.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,49),root.show_gradient(G_1.value,G_2.value,49),root.show_gradient(B_1.value,B_2.value,49),root.show_gradient(T_1.value,T_2.value,49)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,49.5),root.show_gradient(G_1.value,G_2.value,49.5),root.show_gradient(B_1.value,B_2.value,49.5),root.show_gradient(T_1.value,T_2.value,49.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,50),root.show_gradient(G_1.value,G_2.value,50),root.show_gradient(B_1.value,B_2.value,50),root.show_gradient(T_1.value,T_2.value,50)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,50.5),root.show_gradient(G_1.value,G_2.value,50.5),root.show_gradient(B_1.value,B_2.value,50.5),root.show_gradient(T_1.value,T_2.value,50.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,51),root.show_gradient(G_1.value,G_2.value,51),root.show_gradient(B_1.value,B_2.value,51),root.show_gradient(T_1.value,T_2.value,51)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,51.5),root.show_gradient(G_1.value,G_2.value,51.5),root.show_gradient(B_1.value,B_2.value,51.5),root.show_gradient(T_1.value,T_2.value,51.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,52),root.show_gradient(G_1.value,G_2.value,52),root.show_gradient(B_1.value,B_2.value,52),root.show_gradient(T_1.value,T_2.value,52)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,52.5),root.show_gradient(G_1.value,G_2.value,52.5),root.show_gradient(B_1.value,B_2.value,52.5),root.show_gradient(T_1.value,T_2.value,52.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,53),root.show_gradient(G_1.value,G_2.value,53),root.show_gradient(B_1.value,B_2.value,53),root.show_gradient(T_1.value,T_2.value,53)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,53.5),root.show_gradient(G_1.value,G_2.value,53.5),root.show_gradient(B_1.value,B_2.value,53.5),root.show_gradient(T_1.value,T_2.value,53.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,54),root.show_gradient(G_1.value,G_2.value,54),root.show_gradient(B_1.value,B_2.value,54),root.show_gradient(T_1.value,T_2.value,54)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,54.5),root.show_gradient(G_1.value,G_2.value,54.5),root.show_gradient(B_1.value,B_2.value,54.5),root.show_gradient(T_1.value,T_2.value,54.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,55),root.show_gradient(G_1.value,G_2.value,55),root.show_gradient(B_1.value,B_2.value,55),root.show_gradient(T_1.value,T_2.value,55)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,55.5),root.show_gradient(G_1.value,G_2.value,55.5),root.show_gradient(B_1.value,B_2.value,55.5),root.show_gradient(T_1.value,T_2.value,55.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,56),root.show_gradient(G_1.value,G_2.value,56),root.show_gradient(B_1.value,B_2.value,56),root.show_gradient(T_1.value,T_2.value,56)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,56.5),root.show_gradient(G_1.value,G_2.value,56.5),root.show_gradient(B_1.value,B_2.value,56.5),root.show_gradient(T_1.value,T_2.value,56.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,57),root.show_gradient(G_1.value,G_2.value,57),root.show_gradient(B_1.value,B_2.value,57),root.show_gradient(T_1.value,T_2.value,57)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,57.5),root.show_gradient(G_1.value,G_2.value,57.5),root.show_gradient(B_1.value,B_2.value,57.5),root.show_gradient(T_1.value,T_2.value,57.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,58),root.show_gradient(G_1.value,G_2.value,58),root.show_gradient(B_1.value,B_2.value,58),root.show_gradient(T_1.value,T_2.value,58)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,58.5),root.show_gradient(G_1.value,G_2.value,58.5),root.show_gradient(B_1.value,B_2.value,58.5),root.show_gradient(T_1.value,T_2.value,58.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,59),root.show_gradient(G_1.value,G_2.value,59),root.show_gradient(B_1.value,B_2.value,59),root.show_gradient(T_1.value,T_2.value,59)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,59.5),root.show_gradient(G_1.value,G_2.value,59.5),root.show_gradient(B_1.value,B_2.value,59.5),root.show_gradient(T_1.value,T_2.value,59.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,60),root.show_gradient(G_1.value,G_2.value,60),root.show_gradient(B_1.value,B_2.value,60),root.show_gradient(T_1.value,T_2.value,60)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,60.5),root.show_gradient(G_1.value,G_2.value,60.5),root.show_gradient(B_1.value,B_2.value,60.5),root.show_gradient(T_1.value,T_2.value,60.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,61),root.show_gradient(G_1.value,G_2.value,61),root.show_gradient(B_1.value,B_2.value,61),root.show_gradient(T_1.value,T_2.value,61)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,61.5),root.show_gradient(G_1.value,G_2.value,61.5),root.show_gradient(B_1.value,B_2.value,61.5),root.show_gradient(T_1.value,T_2.value,61.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,62),root.show_gradient(G_1.value,G_2.value,62),root.show_gradient(B_1.value,B_2.value,62),root.show_gradient(T_1.value,T_2.value,62)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,62.5),root.show_gradient(G_1.value,G_2.value,62.5),root.show_gradient(B_1.value,B_2.value,62.5),root.show_gradient(T_1.value,T_2.value,62.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,63),root.show_gradient(G_1.value,G_2.value,63),root.show_gradient(B_1.value,B_2.value,63),root.show_gradient(T_1.value,T_2.value,63)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,63.5),root.show_gradient(G_1.value,G_2.value,63.5),root.show_gradient(B_1.value,B_2.value,63.5),root.show_gradient(T_1.value,T_2.value,63.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,64),root.show_gradient(G_1.value,G_2.value,64),root.show_gradient(B_1.value,B_2.value,64),root.show_gradient(T_1.value,T_2.value,64)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,64.5),root.show_gradient(G_1.value,G_2.value,64.5),root.show_gradient(B_1.value,B_2.value,64.5),root.show_gradient(T_1.value,T_2.value,64.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,65),root.show_gradient(G_1.value,G_2.value,65),root.show_gradient(B_1.value,B_2.value,65),root.show_gradient(T_1.value,T_2.value,65)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,65.5),root.show_gradient(G_1.value,G_2.value,65.5),root.show_gradient(B_1.value,B_2.value,65.5),root.show_gradient(T_1.value,T_2.value,65.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,66),root.show_gradient(G_1.value,G_2.value,66),root.show_gradient(B_1.value,B_2.value,66),root.show_gradient(T_1.value,T_2.value,66)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,66.5),root.show_gradient(G_1.value,G_2.value,66.5),root.show_gradient(B_1.value,B_2.value,66.5),root.show_gradient(T_1.value,T_2.value,66.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,67),root.show_gradient(G_1.value,G_2.value,67),root.show_gradient(B_1.value,B_2.value,67),root.show_gradient(T_1.value,T_2.value,67)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,67.5),root.show_gradient(G_1.value,G_2.value,67.5),root.show_gradient(B_1.value,B_2.value,67.5),root.show_gradient(T_1.value,T_2.value,67.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,68),root.show_gradient(G_1.value,G_2.value,68),root.show_gradient(B_1.value,B_2.value,68),root.show_gradient(T_1.value,T_2.value,68)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,68.5),root.show_gradient(G_1.value,G_2.value,68.5),root.show_gradient(B_1.value,B_2.value,68.5),root.show_gradient(T_1.value,T_2.value,68.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,69),root.show_gradient(G_1.value,G_2.value,69),root.show_gradient(B_1.value,B_2.value,69),root.show_gradient(T_1.value,T_2.value,69)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,69.5),root.show_gradient(G_1.value,G_2.value,69.5),root.show_gradient(B_1.value,B_2.value,69.5),root.show_gradient(T_1.value,T_2.value,69.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,70),root.show_gradient(G_1.value,G_2.value,70),root.show_gradient(B_1.value,B_2.value,70),root.show_gradient(T_1.value,T_2.value,70)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,70.5),root.show_gradient(G_1.value,G_2.value,70.5),root.show_gradient(B_1.value,B_2.value,70.5),root.show_gradient(T_1.value,T_2.value,70.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,71),root.show_gradient(G_1.value,G_2.value,71),root.show_gradient(B_1.value,B_2.value,71),root.show_gradient(T_1.value,T_2.value,71)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,71.5),root.show_gradient(G_1.value,G_2.value,71.5),root.show_gradient(B_1.value,B_2.value,71.5),root.show_gradient(T_1.value,T_2.value,71.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,72),root.show_gradient(G_1.value,G_2.value,72),root.show_gradient(B_1.value,B_2.value,72),root.show_gradient(T_1.value,T_2.value,72)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,72.5),root.show_gradient(G_1.value,G_2.value,72.5),root.show_gradient(B_1.value,B_2.value,72.5),root.show_gradient(T_1.value,T_2.value,72.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,73),root.show_gradient(G_1.value,G_2.value,73),root.show_gradient(B_1.value,B_2.value,73),root.show_gradient(T_1.value,T_2.value,73)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,73.5),root.show_gradient(G_1.value,G_2.value,73.5),root.show_gradient(B_1.value,B_2.value,73.5),root.show_gradient(T_1.value,T_2.value,73.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,74),root.show_gradient(G_1.value,G_2.value,74),root.show_gradient(B_1.value,B_2.value,74),root.show_gradient(T_1.value,T_2.value,74)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,74.5),root.show_gradient(G_1.value,G_2.value,74.5),root.show_gradient(B_1.value,B_2.value,74.5),root.show_gradient(T_1.value,T_2.value,74.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,75),root.show_gradient(G_1.value,G_2.value,75),root.show_gradient(B_1.value,B_2.value,75),root.show_gradient(T_1.value,T_2.value,75)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,75.5),root.show_gradient(G_1.value,G_2.value,75.5),root.show_gradient(B_1.value,B_2.value,75.5),root.show_gradient(T_1.value,T_2.value,75.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,76),root.show_gradient(G_1.value,G_2.value,76),root.show_gradient(B_1.value,B_2.value,76),root.show_gradient(T_1.value,T_2.value,76)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,76.5),root.show_gradient(G_1.value,G_2.value,76.5),root.show_gradient(B_1.value,B_2.value,76.5),root.show_gradient(T_1.value,T_2.value,76.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,77),root.show_gradient(G_1.value,G_2.value,77),root.show_gradient(B_1.value,B_2.value,77),root.show_gradient(T_1.value,T_2.value,77)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,77.5),root.show_gradient(G_1.value,G_2.value,77.5),root.show_gradient(B_1.value,B_2.value,77.5),root.show_gradient(T_1.value,T_2.value,77.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,78),root.show_gradient(G_1.value,G_2.value,78),root.show_gradient(B_1.value,B_2.value,78),root.show_gradient(T_1.value,T_2.value,78)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,78.5),root.show_gradient(G_1.value,G_2.value,78.5),root.show_gradient(B_1.value,B_2.value,78.5),root.show_gradient(T_1.value,T_2.value,78.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,79),root.show_gradient(G_1.value,G_2.value,79),root.show_gradient(B_1.value,B_2.value,79),root.show_gradient(T_1.value,T_2.value,79)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,79.5),root.show_gradient(G_1.value,G_2.value,79.5),root.show_gradient(B_1.value,B_2.value,79.5),root.show_gradient(T_1.value,T_2.value,79.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,80),root.show_gradient(G_1.value,G_2.value,80),root.show_gradient(B_1.value,B_2.value,80),root.show_gradient(T_1.value,T_2.value,80)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,80.5),root.show_gradient(G_1.value,G_2.value,80.5),root.show_gradient(B_1.value,B_2.value,80.5),root.show_gradient(T_1.value,T_2.value,80.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,81),root.show_gradient(G_1.value,G_2.value,81),root.show_gradient(B_1.value,B_2.value,81),root.show_gradient(T_1.value,T_2.value,81)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,81.5),root.show_gradient(G_1.value,G_2.value,81.5),root.show_gradient(B_1.value,B_2.value,81.5),root.show_gradient(T_1.value,T_2.value,81.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,82),root.show_gradient(G_1.value,G_2.value,82),root.show_gradient(B_1.value,B_2.value,82),root.show_gradient(T_1.value,T_2.value,82)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,82.5),root.show_gradient(G_1.value,G_2.value,82.5),root.show_gradient(B_1.value,B_2.value,82.5),root.show_gradient(T_1.value,T_2.value,82.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,83),root.show_gradient(G_1.value,G_2.value,83),root.show_gradient(B_1.value,B_2.value,83),root.show_gradient(T_1.value,T_2.value,83)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,83.5),root.show_gradient(G_1.value,G_2.value,83.5),root.show_gradient(B_1.value,B_2.value,83.5),root.show_gradient(T_1.value,T_2.value,83.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,84),root.show_gradient(G_1.value,G_2.value,84),root.show_gradient(B_1.value,B_2.value,84),root.show_gradient(T_1.value,T_2.value,84)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,84.5),root.show_gradient(G_1.value,G_2.value,84.5),root.show_gradient(B_1.value,B_2.value,84.5),root.show_gradient(T_1.value,T_2.value,84.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,85),root.show_gradient(G_1.value,G_2.value,85),root.show_gradient(B_1.value,B_2.value,85),root.show_gradient(T_1.value,T_2.value,85)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,85.5),root.show_gradient(G_1.value,G_2.value,85.5),root.show_gradient(B_1.value,B_2.value,85.5),root.show_gradient(T_1.value,T_2.value,85.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,86),root.show_gradient(G_1.value,G_2.value,86),root.show_gradient(B_1.value,B_2.value,86),root.show_gradient(T_1.value,T_2.value,86)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,86.5),root.show_gradient(G_1.value,G_2.value,86.5),root.show_gradient(B_1.value,B_2.value,86.5),root.show_gradient(T_1.value,T_2.value,86.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,87),root.show_gradient(G_1.value,G_2.value,87),root.show_gradient(B_1.value,B_2.value,87),root.show_gradient(T_1.value,T_2.value,87)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,87.5),root.show_gradient(G_1.value,G_2.value,87.5),root.show_gradient(B_1.value,B_2.value,87.5),root.show_gradient(T_1.value,T_2.value,87.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,88),root.show_gradient(G_1.value,G_2.value,88),root.show_gradient(B_1.value,B_2.value,88),root.show_gradient(T_1.value,T_2.value,88)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,88.5),root.show_gradient(G_1.value,G_2.value,88.5),root.show_gradient(B_1.value,B_2.value,88.5),root.show_gradient(T_1.value,T_2.value,88.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,89),root.show_gradient(G_1.value,G_2.value,89),root.show_gradient(B_1.value,B_2.value,89),root.show_gradient(T_1.value,T_2.value,89)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,89.5),root.show_gradient(G_1.value,G_2.value,89.5),root.show_gradient(B_1.value,B_2.value,89.5),root.show_gradient(T_1.value,T_2.value,89.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,90),root.show_gradient(G_1.value,G_2.value,90),root.show_gradient(B_1.value,B_2.value,90),root.show_gradient(T_1.value,T_2.value,90)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,90.5),root.show_gradient(G_1.value,G_2.value,90.5),root.show_gradient(B_1.value,B_2.value,90.5),root.show_gradient(T_1.value,T_2.value,90.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,91),root.show_gradient(G_1.value,G_2.value,91),root.show_gradient(B_1.value,B_2.value,91),root.show_gradient(T_1.value,T_2.value,91)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,91.5),root.show_gradient(G_1.value,G_2.value,91.5),root.show_gradient(B_1.value,B_2.value,91.5),root.show_gradient(T_1.value,T_2.value,91.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,92),root.show_gradient(G_1.value,G_2.value,92),root.show_gradient(B_1.value,B_2.value,92),root.show_gradient(T_1.value,T_2.value,92)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,92.5),root.show_gradient(G_1.value,G_2.value,92.5),root.show_gradient(B_1.value,B_2.value,92.5),root.show_gradient(T_1.value,T_2.value,92.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,93),root.show_gradient(G_1.value,G_2.value,93),root.show_gradient(B_1.value,B_2.value,93),root.show_gradient(T_1.value,T_2.value,93)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,93.5),root.show_gradient(G_1.value,G_2.value,93.5),root.show_gradient(B_1.value,B_2.value,93.5),root.show_gradient(T_1.value,T_2.value,93.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,94),root.show_gradient(G_1.value,G_2.value,94),root.show_gradient(B_1.value,B_2.value,94),root.show_gradient(T_1.value,T_2.value,94)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,94.5),root.show_gradient(G_1.value,G_2.value,94.5),root.show_gradient(B_1.value,B_2.value,94.5),root.show_gradient(T_1.value,T_2.value,94.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,95),root.show_gradient(G_1.value,G_2.value,95),root.show_gradient(B_1.value,B_2.value,95),root.show_gradient(T_1.value,T_2.value,95)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,95.5),root.show_gradient(G_1.value,G_2.value,95.5),root.show_gradient(B_1.value,B_2.value,95.5),root.show_gradient(T_1.value,T_2.value,95.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,96),root.show_gradient(G_1.value,G_2.value,96),root.show_gradient(B_1.value,B_2.value,96),root.show_gradient(T_1.value,T_2.value,96)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,96.5),root.show_gradient(G_1.value,G_2.value,96.5),root.show_gradient(B_1.value,B_2.value,96.5),root.show_gradient(T_1.value,T_2.value,96.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,97),root.show_gradient(G_1.value,G_2.value,97),root.show_gradient(B_1.value,B_2.value,97),root.show_gradient(T_1.value,T_2.value,97)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,97.5),root.show_gradient(G_1.value,G_2.value,97.5),root.show_gradient(B_1.value,B_2.value,97.5),root.show_gradient(T_1.value,T_2.value,97.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,98),root.show_gradient(G_1.value,G_2.value,98),root.show_gradient(B_1.value,B_2.value,98),root.show_gradient(T_1.value,T_2.value,98)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,98.5),root.show_gradient(G_1.value,G_2.value,98.5),root.show_gradient(B_1.value,B_2.value,98.5),root.show_gradient(T_1.value,T_2.value,98.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,99),root.show_gradient(G_1.value,G_2.value,99),root.show_gradient(B_1.value,B_2.value,99),root.show_gradient(T_1.value,T_2.value,99)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,99.5),root.show_gradient(G_1.value,G_2.value,99.5),root.show_gradient(B_1.value,B_2.value,99.5),root.show_gradient(T_1.value,T_2.value,99.5)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                Label:
                    text:''
                    canvas.before:
                        Color:
                            rgba:root.show_gradient(R_1.value,R_2.value,100),root.show_gradient(G_1.value,G_2.value,100),root.show_gradient(B_1.value,B_2.value,100),root.show_gradient(T_1.value,T_2.value,100)
                        Rectangle:
                            size:self.size
                            pos:self.pos
        BoxLayout:
            size_hint:1,.2
            Label:
                text:"Click to Copy Convenient Value"
                color:1,1,1,.7
        BoxLayout:
            size_hint:1,.25
            Button:
                id:main_preview_blend
                text:root.show_color_result(R_1.value,G_1.value,B_1.value,T_1.value,R_2.value,G_2.value,B_2.value,T_2.value,switch3.active,root.color_value)
                background_normal:'5.png'
                on_release: Clipboard.copy(self.text)
<lang>:
    name: 'lang'
    id:lang
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation: "vertical"
        BoxLayout:
            padding:("15dp","15dp","15dp","0dp")
            Label:
                id:lang_label
                text:root.manager.screens[1].color_value
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'3.png'
        BoxLayout:
            padding:("15dp","15dp","15dp","15dp")
            size_hint:1,.5
            Label:
                text:"Select Language"
        BoxLayout:
            size_hint:1,.5
            padding:("0dp","15dp","0dp","15dp")
            orientation:'horizontal'
            BoxLayout:
                padding:("15dp","0dp","7.5dp","0dp")
                Button:
                    id:set_hexa
                    text:'hexa'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("hexa")
                        root.manager.screens[1].color_value = str('hexa')
            BoxLayout:
                padding:("7.5dp","0dp","7.5dp","0dp")
                Button:
                    id:set_rgba
                    text:'rgba'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("rgba")
                        root.manager.screens[1].color_value = str('rgba')
            BoxLayout:
                padding:("7.5dp","0dp","15dp","0dp")
                Button:
                    id:set_kivy
                    text:'Kivy'
                    halign: 'center'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("kivy")
                        root.manager.screens[1].color_value = str('kivy')
        BoxLayout:
            padding:("15dp","0dp","15dp","15dp")
            Button:
                id:lang_button
                text:"Done"
                background_normal: '1.png'
                on_release:
                    root.manager.screens[1].color_value = lang_label.text
                    root.manager.transition.direction = 'right'
                    app.root.current = 'RGB'
<lang_2>:
    name: 'lang_2'
    id:lang_2
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation: "vertical"
        BoxLayout:
            padding:("15dp","15dp","15dp","0dp")
            Label:
                id:lang_label
                text:root.manager.screens[2].color_value
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'3.png'
        BoxLayout:
            padding:("15dp","15dp","15dp","15dp")
            size_hint:1,.5
            Label:
                text:"Select Language"
        BoxLayout:
            size_hint:1,.5
            padding:("0dp","15dp","0dp","15dp")
            orientation:'horizontal'
            BoxLayout:
                padding:("15dp","0dp","7.5dp","0dp")
                Button:
                    id:set_hexa
                    text:'hexa'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("hexa")
                        root.manager.screens[2].color_value = str('hexa')
            BoxLayout:
                padding:("7.5dp","0dp","7.5dp","0dp")
                Button:
                    id:set_rgba
                    text:'rgba'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("rgba")
                        root.manager.screens[2].color_value = str('rgba')
            BoxLayout:
                padding:("7.5dp","0dp","15dp","0dp")
                Button:
                    id:set_kivy
                    text:'Kivy'
                    halign: 'center'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("kivy")
                        root.manager.screens[2].color_value = str('kivy')
        BoxLayout:
            padding:("15dp","0dp","15dp","15dp")
            Button:
                id:lang_button
                text:"Done"
                background_normal: '1.png'
                on_release:
                    root.manager.screens[2].color_value = lang_label.text
                    root.manager.transition.direction = 'right'
                    app.root.current = 'VIBGYR'
<lang_3>:
    name: 'lang_3'
    id:lang_3
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation: "vertical"
        BoxLayout:
            padding:("15dp","15dp","15dp","0dp")
            Label:
                id:lang_label
                text:root.manager.screens[3].color_value
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'3.png'
        BoxLayout:
            size_hint:1,.5
            padding:("15dp","15dp","15dp","15dp")
            size_hint:1,.5
            Label:
                text:"Select Language"
        BoxLayout:
            size_hint:1,.5
            padding:("0dp","15dp","0dp","15dp")
            orientation:'horizontal'
            BoxLayout:
                padding:("15dp","0dp","7.5dp","0dp")
                Button:
                    id:set_hexa
                    text:'hexa'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("hexa")
                        root.manager.screens[3].color_value = str('hexa')
            BoxLayout:
                padding:("7.5dp","0dp","7.5dp","0dp")
                Button:
                    id:set_rgba
                    text:'rgba'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("rgba")
                        root.manager.screens[3].color_value = str('rgba')
            BoxLayout:
                padding:("7.5dp","0dp","15dp","0dp")
                Button:
                    id:set_kivy
                    text:'Kivy'
                    halign: 'center'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("kivy")
                        root.manager.screens[3].color_value = str('kivy')
        BoxLayout:
            padding:("15dp","0dp","15dp","15dp")
            Button:
                id:lang_button
                text:"Done"
                background_normal: '1.png'
                on_release:
                    root.manager.screens[3].color_value = lang_label.text
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Blender'
<lang_4>:
    name: 'lang_4'
    id:lang_4
    BoxLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        orientation: "vertical"
        BoxLayout:
            padding:("15dp","15dp","15dp","0dp")
            Label:
                id:lang_label
                text:root.manager.screens[4].color_value
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'3.png'
        BoxLayout:
            padding:("15dp","15dp","15dp","15dp")
            size_hint:1,.5
            Label:
                text:"Select Language"
        BoxLayout:
            size_hint:1,.5
            padding:("0dp","15dp","0dp","15dp")
            orientation:'horizontal'
            BoxLayout:
                padding:("15dp","0dp","7.5dp","0dp")
                Button:
                    id:set_hexa
                    text:'hexa'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("hexa")
                        root.manager.screens[4].color_value = str('hexa')
            BoxLayout:
                padding:("7.5dp","0dp","7.5dp","0dp")
                Button:
                    id:set_rgba
                    text:'rgba'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("rgba")
                        root.manager.screens[4].color_value = str('rgba')
            BoxLayout:
                padding:("7.5dp","0dp","15dp","0dp")
                Button:
                    id:set_rgba
                    text:'kivy'
                    background_normal: '4.png'
                    on_release:
                        lang_label.text = str("kivy")
                        root.manager.screens[4].color_value = str('kivy')
        BoxLayout:
            padding:("15dp","0dp","15dp","15dp")
            Button:
                id:lang_button
                text:"Done"
                background_normal: '1.png'
                on_release:
                    root.manager.screens[4].color_value = lang_label.text
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Gradient'
<Theory>:
    name: 'Theory'
    id:Theory
    BoxLayout:
        orientation:'vertical'
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        BoxLayout:
            orientation:"horizontal"
            size_hint: 1,.098
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'Theory'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        BoxLayout:
            size_hint:1,.2
            Label:
                text:'LOG IN'
                color:1,1,1,1
                font_size:'20dp'
        BoxLayout:
            size_hint:1,.1
            padding:("15dp","0dp","15dp","0dp")
            orientation:'horizontal'
            TextInput:
                id:t1
                text:'Username'
                multiline: False
                on_text_validate:t1.text = 'Wrong!'
            TextInput:
                id:t2
                text:'Password'
                multiline: False
                on_text_validate: t2.text = 'Wrong!'
        BoxLayout:
            size_hint:1,1
            Label:
                text:''
<About>:
    name: 'About'
    id:About
    BoxLayout:
        orientation:'vertical'
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'bg2.png'
        BoxLayout:
            orientation:"horizontal"
            size_hint: 1,.113
            Button:
                size_hint:.3,1
                text:"Home"
                background_normal: '3.png'
                on_release:
                    root.manager.transition.direction = 'right'
                    app.root.current = 'Menu'
            Label:
                text:'About'
                canvas.before:
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:'5.png'
        BoxLayout:
            size_hint:1,.5
            padding:('15dp','15dp','15dp','15dp')
            orientation:'vertical'
            Label:
                text:'App creator  :  rafi.riday@gmail.com' + root.br + root.br + 'Purpose        :' + root.br + '        Color Picker' + root.br + '        Blending & Gradients' + root.br + '        Visualisation Theory' + root.br + '        Creative Systems' + root.br + root.br + 'App Version : 1.5.5'
        BoxLayout:
            size_hint:1,1
            Label:
                text:''
'''
class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)
    def on_key(self, window, key, *args):
        if key == 27:
            if self.current_screen.name == "Menu":
                return False
            elif self.current_screen.name == "RGB":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "VIBGYR":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "Blender":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "Gradient":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "About":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "Theory":
                self.transition.direction = 'right'
                self.current = "Menu"
                return True
            elif self.current_screen.name == "lang":
                self.transition.direction = 'right'
                self.current = "RGB"
                return True
            elif self.current_screen.name == "lang_2":
                self.transition.direction = 'right'
                self.current = "VIBGYR"
                return True
            elif self.current_screen.name == "lang_3":
                self.transition.direction = 'right'
                self.current = "Blender"
                return True
            elif self.current_screen.name == "lang_4":
                self.transition.direction = 'right'
                self.current = "Gradient"
                return True
class Menu(Screen):
    pass
class RGB(Screen):
    color_value=StringProperty("rgba")
    def all_type(self, d1, d2, d3, d4, a, id):
        if id=='rgba':
            if a==True:
                rgba=str("rgba(%.0f, %.0f, %.0f, %.2f)" % (d1 * 2.55,d2 * 2.55,d3 * 2.55,d4 / 100 ))
            else:
                rgba=str("rgb(%.0f, %.0f, %.0f)" % (d1 * 2.55,d2 * 2.55,d3 * 2.55))
            return rgba
        if id=='hexa':
            if a==True:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2) + format(int(d4 * 2.555), 'x').zfill(2))
            else:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2))
            return hexa
        if id=='kivy':
            if a==True:
                kivy=str("%.2f, %.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100, d4 / 100))
            else:
                kivy=str("%.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100))
            return kivy
    def main_processor(self, id, value_slider_main):
        for i in range(1,10):
            if id=="red":
                if value_slider_main>=0 and value_slider_main<=10:
                    return 1
                if value_slider_main==int(10+i):
                    return float(1 - (i/10))
                if value_slider_main>=20 and value_slider_main<=40:
                    return 0
                if value_slider_main==int(40+i):
                    return float(i/10)
                if value_slider_main>=50 and value_slider_main<=60:
                    return 1
            if id=="green":
                if value_slider_main==0:
                    return 0
                if value_slider_main==int(i):
                    return float(i/10)
                if value_slider_main>=10 and value_slider_main<=30:
                    return 1
                if value_slider_main==int(30+i):
                    return float(1 - (i/10))
                if value_slider_main>=40 and value_slider_main<=60:
                    return 0
            if id=="blue":
                if value_slider_main>=0 and value_slider_main<=20:
                    return 0
                if value_slider_main==int(20+i):
                    return float(i/10)
                if value_slider_main>=30 and value_slider_main<=50:
                    return 1
                if value_slider_main==int(50+i):
                    return float(1 - (i/10))
                if value_slider_main==60:
                    return 0
    def re_processor(self, main_color, value):
        if value>=0 and value<=99:
            return float(1 - ((1 - main_color) * (value / 100)))
        if value>=100 and value<=109:
            return main_color
        if value>=110 and value<=209:
            return float(main_color - (main_color * ((value - 109) / 100)))
    def transperancy(self, active, value):
        if active==True:
            return value
        else:
            return float(1)
class VIBGYR(Screen):
    color_value=StringProperty("rgba")
    def VIBGYR(self,V,I,B,G,Y,R,T,a,id):
        B=100-B
        V=100-V
        Y=100-Y
        F_r=(B+R)/2
        F_g=(V+G)/2
        F_b=(Y+I)/2
        if a==True:
            if id=="rgba":
                F_r=float(F_r*2.55)
                F_g=float(F_g*2.55)
                F_b=float(F_b*2.55)
                T=float(T/100)
                return str("rgba(%.0f, %.0f, %.0f, %.2f)" % (F_r,F_g,F_b,T))
            if id=="hexa":
                hexa=str('#' + format(int(F_r * 2.555), 'x').zfill(2) + format(int(F_g * 2.555), 'x').zfill(2) + format(int(F_b * 2.555), 'x').zfill(2) + format(int(T * 2.555), 'x').zfill(2))
                return hexa
            if id=="kivy":
                F_r=float(F_r/100)
                F_g=float(F_g/100)
                F_b=float(F_b/100)
                T=float(T/100)
                return str("%.2f, %.2f, %.2f, %.2f" % (F_r, F_g, F_b, T))
        else:
            if id=="rgba":
                F_r=float(F_r*2.55)
                F_g=float(F_g*2.55)
                F_b=float(F_b*2.55)
                T=float(T/100)
                return str("rgba(%.0f, %.0f, %.0f)" % (F_r,F_g,F_b))
            if id=="hexa":
                hexa=str('#' + format(int(F_r * 2.555), 'x').zfill(2) + format(int(F_g * 2.555), 'x').zfill(2) + format(int(F_b * 2.555), 'x').zfill(2))
                return hexa
            if id=="kivy":
                F_r=float(F_r/100)
                F_g=float(F_g/100)
                F_b=float(F_b/100)
                T=float(T/100)
                return str("%.2f, %.2f, %.2f" % (F_r, F_g, F_b))
    def VIBGYR_preview(self,V,I,B,G,Y,R,T,a):
        B=100-B
        V=100-V
        Y=100-Y
        F_r=(B+R)/2
        F_g=(V+G)/2
        F_b=(Y+I)/2
        F_r=float(F_r/100)
        F_g=float(F_g/100)
        F_b=float(F_b/100)
        if a==True:
            T=float(T/100)
        else:
            T=float(1)
        return (F_r, F_g, F_b, T)
    def transperancy(self, active, value):
        if active==True:
            return value
        else:
            return float(1)
class Blender(Screen):
    color_value=StringProperty("rgba")
    def show_color_single(self, d1, d2, d3, d4, a, id):
        if id=='rgba':
            if a==True:
                rgba=str("%.0f, %.0f, %.0f, %.2f" % (d1 * 2.55,d2 * 2.55,d3 * 2.55,d4 / 100))
            else:
                rgba=str("%.0f, %.0f, %.0f" % (d1 * 2.55,d2 * 2.55,d3 * 2.55))
            return rgba
        if id=='hexa':
            if a==True:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2) + format(int(d4 * 2.555), 'x').zfill(2))
            else:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2))
            return hexa
        if id=='kivy':
            if a==True:
                kivy=str("%.2f, %.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100, d4 / 100))
            else:
                kivy=str("%.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100))
            return kivy
    def show_color_result(self, r1, g1, b1, t1, r2, g2, b2, t2, a, id):
        d1=(r1+r2)/2
        d2=(g1+g2)/2
        d3=(b1+b2)/2
        d4=(t1+t2)/2
        if id=='rgba':
            if a==True:
                rgba=str("rgba(%.0f, %.0f, %.0f, %.2f)" % (d1 * 2.55,d2 * 2.55,d3 * 2.55,d4 / 100 ))
            else:
                rgba=str("rgb(%.0f, %.0f, %.0f)" % (d1 * 2.55,d2 * 2.55,d3 * 2.55))
            return rgba
        if id=='hexa':
            if a==True:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2) + format(int(d4 * 2.555), 'x').zfill(2))
            else:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2))
            return hexa
        if id=='kivy':
            if a==True:
                kivy=str("%.2f, %.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100, d4 / 100))
            else:
                kivy=str("%.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100))
            return kivy
    def transperancy(self, active, value):
        if active==True:
            return value
        else:
            return float(1)
class Gradient(Screen):
    color_value=StringProperty("rgba")
    def show_color_single(self, d1, d2, d3, d4, a, id):
        if id=='rgba':
            if a==True:
                rgba=str("%.0f, %.0f, %.0f, %.2f" % (d1 * 2.55,d2 * 2.55,d3 * 2.55,d4 / 100 ))
            else:
                rgba=str("%.0f, %.0f, %.0f" % (d1 * 2.55,d2 * 2.55,d3 * 2.55))
            return rgba
        if id=='hexa':
            if a==True:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2) + format(int(d4 * 2.555), 'x').zfill(2))
            else:
                hexa=str('#' + format(int(d1 * 2.555), 'x').zfill(2) + format(int(d2 * 2.555), 'x').zfill(2) + format(int(d3 * 2.555), 'x').zfill(2))
            return hexa
        if id=='kivy':
            if a==True:
                kivy=str("%.2f, %.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100, d4 / 100))
            else:
                kivy=str("%.2f, %.2f, %.2f" % (d1 / 100, d2 / 100, d3 / 100))
            return kivy
    def show_color_result(self, r1, g1, b1, t1, r2, g2, b2, t2, a, id):
        if id=='rgba':
            if a==True:
                rgba=str("rgba(%.0f, %.0f, %.0f, %.2f) , rgba(%.0f, %.0f, %.0f, %.2f)" % (r1 * 2.55,g1 * 2.55,b1 * 2.55,t1 / 100,r2 * 2.55,g2 * 2.55,b2 * 2.55,t2 / 100))
            else:
                rgba=str("rgb(%.0f, %.0f, %.0f) , rgb(%.0f, %.0f, %.0f)" % (r1 * 2.55,g1 * 2.55,b1 * 2.55,r2 * 2.55,g2 * 2.55,b2 * 2.55))
            return rgba
        if id=='hexa':
            if a==True:
                hexa=str('#' + format(int(r1 * 2.555), 'x').zfill(2) + format(int(g1 * 2.555), 'x').zfill(2) + format(int(b1 * 2.555), 'x').zfill(2) + format(int(t1 * 2.555), 'x').zfill(2) + ' , ' + '#' + format(int(r2 * 2.555), 'x').zfill(2) + format(int(g2 * 2.555), 'x').zfill(2) + format(int(b2 * 2.555), 'x').zfill(2) + format(int(t2 * 2.555), 'x').zfill(2))
            else:
                hexa=str('#' + format(int(r1 * 2.555), 'x').zfill(2) + format(int(g1 * 2.555), 'x').zfill(2) + format(int(b1 * 2.555), 'x').zfill(2) + ' , ' + '#' + format(int(r2 * 2.555), 'x').zfill(2) + format(int(g2 * 2.555), 'x').zfill(2) + format(int(b2 * 2.555), 'x').zfill(2))
            return hexa
        if id=='kivy':
            if a==True:
                kivy=str("(%.2f, %.2f, %.2f, %.2f) , (%.2f, %.2f, %.2f, %.2f)" % (r1 / 100,g1 / 100,b1 / 100,t1 / 100,r2 / 100,g2 / 100,b2 / 100,t2 / 100))
            else:
                kivy=str("(%.2f, %.2f, %.2f) , (%.2f, %.2f, %.2f)" % (r1 / 100,g1 / 100,b1 / 100,r2 / 100,g2 / 100,b2 / 100))
            return kivy
    def transperancy(self, active, value):
        if active==True:
            return value
        else:
            return float(1)
    def show_gradient(self, d1, d2, value):
        return float(float(float(d1 / 100) * float(float(100-float(value)) * float(.01))) + float(float(d2 / 100) * float(float(value) * float(.01))))
class lang(Screen):
    pass
class lang_2(Screen):
    pass
class lang_3(Screen):
    pass
class lang_4(Screen):
    pass
class Theory(Screen):
    pass
class About(Screen):
    br=StringProperty('\n')
class CPApp(App):
    def build(self):
        self.icon = 'icon.png'
        screen = Builder.load_string(KV)
        return screen
CPApp().run()