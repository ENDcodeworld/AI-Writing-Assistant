from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

from ai_engine import AIWritingEngine


class StyledButton(Button):
    """自定义样式按钮"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = get_color_from_hex('#4A90E2')
        self.color = get_color_from_hex('#FFFFFF')
        self.font_size = dp(16)
        self.size_hint_y = None
        self.height = dp(50)


class StyledLabel(Label):
    """自定义样式标签"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = get_color_from_hex('#333333')
        self.font_size = dp(14)
        self.text_size = (Window.width - dp(40), None)
        self.halign = 'left'
        self.valign = 'top'


class AIWritingApp(App):
    """AI写作助手APP"""
    
    def build(self):
        self.engine = AIWritingEngine()
        self.title = 'AI智能写作助手'
        
        # 设置窗口背景色
        Window.clearcolor = get_color_from_hex('#F5F5F5')
        
        # 主布局
        self.root = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # 标题
        title_label = Label(
            text='📝 AI智能写作助手',
            font_size=dp(28),
            color=get_color_from_hex('#2C3E50'),
            size_hint_y=None,
            height=dp(60),
            bold=True
        )
        self.root.add_widget(title_label)
        
        # 功能选择区域
        func_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))
        
        self.func_spinner = Spinner(
            text='选择功能',
            values=['文章生成', '营销文案', '论文助手', '诗歌创作'],
            size_hint=(0.5, None),
            height=dp(50),
            background_color=get_color_from_hex('#6C5CE7')
        )
        self.func_spinner.bind(text=self.on_function_change)
        func_box.add_widget(self.func_spinner)
        
        # 风格选择
        self.style_spinner = Spinner(
            text='选择风格',
            values=['科技', '商业', '生活'],
            size_hint=(0.5, None),
            height=dp(50),
            background_color=get_color_from_hex('#00B894')
        )
        func_box.add_widget(self.style_spinner)
        
        self.root.add_widget(func_box)
        
        # 输入区域
        input_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(120), spacing=dp(5))
        
        input_label = Label(
            text='输入主题/关键词：',
            font_size=dp(16),
            color=get_color_from_hex('#2C3E50'),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        input_box.add_widget(input_label)
        
        self.topic_input = TextInput(
            hint_text='例如：人工智能、健康管理、秋天的思念...',
            multiline=False,
            font_size=dp(16),
            padding=[dp(15), dp(15)],
            background_color=get_color_from_hex('#FFFFFF'),
            foreground_color=get_color_from_hex('#2C3E50'),
            cursor_color=get_color_from_hex('#4A90E2'),
            size_hint_y=None,
            height=dp(80)
        )
        input_box.add_widget(self.topic_input)
        
        self.root.add_widget(input_box)
        
        # 生成按钮
        generate_btn = StyledButton(
            text='✨ 开始生成',
            background_color=get_color_from_hex('#E74C3C')
        )
        generate_btn.bind(on_press=self.generate_content)
        self.root.add_widget(generate_btn)
        
        # 结果显示区域
        result_label = Label(
            text='生成结果：',
            font_size=dp(16),
            color=get_color_from_hex('#2C3E50'),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        self.root.add_widget(result_label)
        
        # 滚动视图
        scroll_view = ScrollView(size_hint=(1, 1))
        
        self.result_label = Label(
            text='点击"开始生成"按钮，AI将为您创作内容...',
            font_size=dp(14),
            color=get_color_from_hex('#555555'),
            text_size=(Window.width - dp(40), None),
            halign='left',
            valign='top',
            markup=True,
            size_hint_y=None
        )
        self.result_label.bind(texture_size=self.result_label.setter('size'))
        
        scroll_view.add_widget(self.result_label)
        self.root.add_widget(scroll_view)
        
        # 底部按钮
        bottom_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))
        
        copy_btn = StyledButton(
            text='📋 复制内容',
            background_color=get_color_from_hex('#0984E3'),
            size_hint=(0.5, None)
        )
        copy_btn.bind(on_press=self.copy_content)
        bottom_box.add_widget(copy_btn)
        
        clear_btn = StyledButton(
            text='🗑️ 清空',
            background_color=get_color_from_hex('#636E72'),
            size_hint=(0.5, None)
        )
        clear_btn.bind(on_press=self.clear_content)
        bottom_box.add_widget(clear_btn)
        
        self.root.add_widget(bottom_box)
        
        # VIP提示
        vip_label = Label(
            text='💎 升级VIP解锁更多功能：长文章、高级模板、无广告',
            font_size=dp(12),
            color=get_color_from_hex('#E74C3C'),
            size_hint_y=None,
            height=dp(30)
        )
        self.root.add_widget(vip_label)
        
        return self.root
    
    def on_function_change(self, spinner, text):
        """功能切换时更新风格选项"""
        if text == '文章生成':
            self.style_spinner.values = ['科技', '商业', '生活']
        elif text == '营销文案':
            self.style_spinner.values = ['产品推广', '服务宣传', '活动营销']
        elif text == '论文助手':
            self.style_spinner.values = ['经济学', '管理学', '教育学', '计算机']
        elif text == '诗歌创作':
            self.style_spinner.values = ['现代诗', '古典诗']
        
        self.style_spinner.text = '选择风格'
    
    def generate_content(self, instance):
        """生成内容"""
        topic = self.topic_input.text.strip()
        
        if not topic:
            self.show_popup('提示', '请输入主题或关键词！')
            return
        
        func = self.func_spinner.text
        style = self.style_spinner.text
        
        if func == '选择功能' or style == '选择风格':
            self.show_popup('提示', '请选择功能和风格！')
            return
        
        # 显示加载中
        self.result_label.text = '[b]⏳ AI正在创作中，请稍候...[/b]'
        
        # 生成内容
        try:
            if func == '文章生成':
                style_map = {'科技': 'tech', '商业': 'business', '生活': 'lifestyle'}
                result = self.engine.generate_article(topic, style=style_map.get(style, 'tech'), length='medium')
            
            elif func == '营销文案':
                copy_type_map = {'产品推广': 'product', '服务宣传': 'service', '活动营销': 'activity'}
                result = self.engine.generate_copy(topic, copy_type=copy_type_map.get(style, 'product'))
            
            elif func == '论文助手':
                result = self.engine.generate_essay(topic, field=style)
            
            elif func == '诗歌创作':
                style_map = {'现代诗': 'modern', '古典诗': 'classical'}
                result = self.engine.generate_poetry(topic, style=style_map.get(style, 'modern'))
            
            # 格式化显示结果
            display_text = f"[b]📌 {result['title']}[/b]\n"
            display_text += f"[color=#888888]生成时间: {result['timestamp']}[/color]\n\n"
            display_text += result['content']
            
            if 'word_count' in result:
                display_text += f"\n\n[color=#4A90E2]字数统计: {result['word_count']} 字[/color]"
            
            self.result_label.text = display_text
            
        except Exception as e:
            self.result_label.text = f'[color=#E74C3C]生成失败: {str(e)}[/color]'
    
    def copy_content(self, instance):
        """复制内容到剪贴板"""
        content = self.result_label.text
        # 移除markup标签
        import re
        clean_content = re.sub(r'\[.*?\]', '', content)
        
        # 复制到剪贴板
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(clean_content)
        
        self.show_popup('成功', '内容已复制到剪贴板！')
    
    def clear_content(self, instance):
        """清空内容"""
        self.topic_input.text = ''
        self.result_label.text = '点击"开始生成"按钮，AI将为您创作内容...'
        self.func_spinner.text = '选择功能'
        self.style_spinner.text = '选择风格'
    
    def show_popup(self, title, message):
        """显示弹窗"""
        popup_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        popup_label = Label(text=message, font_size=dp(16))
        popup_layout.add_widget(popup_label)
        
        close_btn = Button(text='确定', size_hint_y=None, height=dp(50))
        popup_layout.add_widget(close_btn)
        
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    AIWritingApp().run()
