# AI智能写作助手
# 支持文章、文案、论文、诗歌一键生成

import random
import json
from datetime import datetime

class AIWritingEngine:
    """AI写作引擎"""
    
    # 写作模板库
    TEMPLATES = {
        'article': {
            'tech': [
                "随着{keyword}技术的不断发展，{industry}行业正在经历深刻的变革。",
                "本文将深入探讨{keyword}在{industry}中的应用现状及未来趋势。",
                "首先，我们需要了解{keyword}的核心原理...",
                "从实际应用来看，{keyword}已经展现出巨大的潜力...",
                "展望未来，{keyword}将成为{industry}发展的重要驱动力。"
            ],
            'business': [
                "在当今竞争激烈的市场环境中，{keyword}已成为企业制胜的关键。",
                "本文将分析{keyword}如何帮助企业提升竞争力。",
                "首先，让我们了解{keyword}的基本概念...",
                "通过实际案例，我们可以看到{keyword}带来的显著效果...",
                "总之，{keyword}是企业实现可持续发展的重要途径。"
            ],
            'lifestyle': [
                "在追求品质生活的今天，{keyword}越来越受到人们的关注。",
                "本文将分享关于{keyword}的实用知识和建议。",
                "首先，我们需要正确认识{keyword}...",
                "在日常生活中，{keyword}可以带来诸多便利...",
                "希望本文能帮助大家更好地理解和应用{keyword}。"
            ]
        },
        'copy': {
            'product': [
                "【爆款推荐】{product}，让您的{benefit}提升{percent}%！",
                "✨ {feature}，{advantage}，{result}！",
                "🔥 限时特惠：原价{price1}，现仅需{price2}！",
                "💯 {guarantee}，{promise}！",
                "立即下单，享受{service}！"
            ],
            'service': [
                "专业{service}，{years}年经验，服务{customers}+客户！",
                "✅ {advantage1}\n✅ {advantage2}\n✅ {advantage3}",
                "📞 24小时在线，{response}分钟内响应！",
                "💰 透明报价，无隐藏费用！",
                "选择我们，就是选择{value}！"
            ],
            'activity': [
                "🎉 {event}盛大开启！",
                "⏰ 活动时间：{start_time} - {end_time}",
                "🎁 {discount}折优惠，满{amount}减{discount_amount}！",
                "🏃‍♂️ 限量{limit}份，先到先得！",
                "📱 扫码参与，立即享受{benefit}！"
            ]
        },
        'essay': {
            'academic': {
                'intro': [
                    "随着{field}研究的不断深入，{topic}已成为学术界关注的热点问题。",
                    "本文旨在探讨{topic}的{aspect}，分析其对{influence}的影响。",
                    "研究{topic}对于{significance}具有重要的理论和实践意义。"
                ],
                'body': [
                    "首先，从理论层面来看，{theory}为{topic}提供了重要的分析框架。",
                    "{scholar}（{year}）指出，{viewpoint}。",
                    "这一观点得到了{data}的支持。",
                    "然而，也有学者提出了不同的看法。{scholar2}（{year2}）认为，{viewpoint2}。",
                    "其次，从实践角度来看，{case}充分说明了{conclusion}。",
                    "数据显示，{statistic}。",
                    "这进一步验证了{validation}。"
                ],
                'conclusion': [
                    "综上所述，{summary}。",
                    "本研究的主要贡献在于{contribution}。",
                    "当然，本研究也存在一定的局限性，如{limitation}。",
                    "未来研究可以进一步探讨{future}。",
                    "相信随着{development}，{topic}将会得到更深入的研究和应用。"
                ]
            }
        },
        'poetry': {
            'modern': [
                "{time}的{place}，\n{weather}，\n{emotion}。",
                "{object}在{action}，\n像{metaphor}。",
                "我{verb}着{noun}，\n想起{memory}。",
                "{scene}，\n{feeling}。",
                "这就是{theme}，\n在{location}。"
            ],
            'classical': [
                "{scene}，\n{weather}。\n{action}，\n{emotion}。"
            ]
        }
    }
    
    # 词汇库
    WORDS = {
        'tech_keywords': ['人工智能', '大数据', '云计算', '物联网', '区块链', '5G', '元宇宙', '量子计算'],
        'business_keywords': ['数字化转型', '品牌战略', '用户体验', '精益管理', '敏捷开发', '增长黑客'],
        'lifestyle_keywords': ['健康生活', '品质消费', '时间管理', '极简主义', '可持续生活', ' mindfulness'],
        'emotions': ['温暖', '忧伤', '激动', '平静', '期待', '怀念', '孤独', '喜悦'],
        'scenes': ['黄昏', '黎明', '雨天', '星空', '海边', '山间', '城市', '乡村'],
        'weather': ['微风轻拂', '细雨绵绵', '阳光明媚', '云雾缭绕', '雪花飘落']
    }
    
    def __init__(self):
        self.history = []
    
    def generate_article(self, topic, style='tech', length='medium'):
        """生成文章"""
        templates = self.TEMPLATES['article'].get(style, self.TEMPLATES['article']['tech'])
        
        # 确定段落数
        para_count = {'short': 3, 'medium': 5, 'long': 7}.get(length, 5)
        
        paragraphs = []
        for i in range(min(para_count, len(templates))):
            template = templates[i]
            content = template.format(
                keyword=topic,
                industry=random.choice(['科技', '商业', '教育', '医疗', '金融'])
            )
            paragraphs.append(content)
        
        # 添加更多内容
        if length == 'long':
            paragraphs.extend([
                f"进一步分析，{topic}在实际应用中展现出显著优势。",
                f"与此同时，我们也需要关注{topic}可能带来的挑战。",
                f"综合来看，{topic}的发展前景十分广阔。"
            ])
        
        article = '\n\n'.join(paragraphs)
        
        # 保存历史
        self._save_history('article', topic, article)
        
        return {
            'title': f"关于{topic}的深入分析",
            'content': article,
            'word_count': len(article),
            'style': style,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def generate_copy(self, product, copy_type='product', **kwargs):
        """生成营销文案"""
        templates = self.TEMPLATES['copy'].get(copy_type, self.TEMPLATES['copy']['product'])
        
        # 填充模板
        copy_parts = []
        for template in templates:
            try:
                part = template.format(
                    product=product,
                    benefit=kwargs.get('benefit', '效率'),
                    percent=kwargs.get('percent', '50'),
                    feature=kwargs.get('feature', '智能算法'),
                    advantage=kwargs.get('advantage', '精准高效'),
                    result=kwargs.get('result', '让您事半功倍'),
                    price1=kwargs.get('price1', '¥999'),
                    price2=kwargs.get('price2', '¥299'),
                    guarantee=kwargs.get('guarantee', '品质保证'),
                    promise=kwargs.get('promise', '不满意全额退款'),
                    service=kwargs.get('service', 'VIP专属服务')
                )
                copy_parts.append(part)
            except:
                copy_parts.append(template)
        
        copy_text = '\n\n'.join(copy_parts)
        
        self._save_history('copy', product, copy_text)
        
        return {
            'title': f"{product}推广文案",
            'content': copy_text,
            'type': copy_type,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def generate_essay(self, topic, field='经济学', academic_level='本科'):
        """生成论文"""
        academic = self.TEMPLATES['essay']['academic']
        
        # 引言
        intro = random.choice(academic['intro']).format(
            field=field,
            topic=topic,
            aspect='发展与影响',
            influence='行业发展',
            significance='推动理论创新和实践应用'
        )
        
        # 正文
        body_paras = []
        for template in academic['body'][:4]:
            try:
                para = template.format(
                    theory='相关理论框架',
                    scholar='张三',
                    year='2023',
                    viewpoint=f'{topic}具有重要的研究价值',
                    data='实证研究数据',
                    scholar2='李四',
                    year2='2022',
                    viewpoint2='需要辩证地看待这个问题',
                    case='典型案例分析',
                    conclusion='这一观点的正确性',
                    statistic='相关统计数据显示',
                    validation='前述观点'
                )
                body_paras.append(para)
            except:
                body_paras.append(template)
        
        body = '\n\n'.join(body_paras)
        
        # 结论
        conclusion = random.choice(academic['conclusion']).format(
            summary=f'本文系统分析了{topic}',
            contribution='提出了新的分析视角',
            limitation='数据样本有待进一步扩大',
            future='更多维度的深入研究',
            development='研究方法的不断完善',
            topic=topic
        )
        
        essay = f"{intro}\n\n{body}\n\n{conclusion}"
        
        self._save_history('essay', topic, essay)
        
        return {
            'title': f"{topic}研究",
            'content': essay,
            'word_count': len(essay),
            'level': academic_level,
            'field': field,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def generate_poetry(self, theme, style='modern'):
        """生成诗歌"""
        templates = self.TEMPLATES['poetry'].get(style, self.TEMPLATES['poetry']['modern'])
        
        lines = []
        for template in templates:
            try:
                line = template.format(
                    time=random.choice(['清晨', '黄昏', '深夜', '午后']),
                    place=random.choice(['公园', '街头', '窗前', '海边']),
                    weather=random.choice(self.WORDS['weather']),
                    emotion=random.choice(self.WORDS['emotions']),
                    object=random.choice(['落叶', '飞鸟', '流云', '孤灯']),
                    action=random.choice(['飘落', '飞过', '飘过', '闪烁']),
                    metaphor=random.choice(['逝去的时光', '远去的梦想', '思念的使者']),
                    verb=random.choice(['抚摸', '凝视', '聆听', '感受']),
                    noun=random.choice(['记忆', '往事', '风景', '心情']),
                    memory=random.choice(['那些年的夏天', '初见时的模样']),
                    scene=random.choice(self.WORDS['scenes']),
                    feeling=random.choice(['心中涌起无限感慨', '嘴角泛起淡淡微笑']),
                    theme=theme,
                    location=random.choice(['这里', '此刻', '心间'])
                )
                lines.append(line)
            except:
                lines.append(template)
        
        poetry = '\n\n'.join(lines)
        
        self._save_history('poetry', theme, poetry)
        
        return {
            'title': f"{theme}",
            'content': poetry,
            'style': style,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def get_history(self):
        """获取历史记录"""
        return self.history
    
    def clear_history(self):
        """清空历史"""
        self.history = []
    
    def _save_history(self, content_type, topic, content):
        """保存到历史"""
        self.history.append({
            'type': content_type,
            'topic': topic,
            'content': content[:100] + '...',  # 只保存前100字
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        # 只保留最近20条
        if len(self.history) > 20:
            self.history = self.history[-20:]


# 测试
if __name__ == '__main__':
    print("=" * 50)
    print("📝 AI智能写作助手测试")
    print("=" * 50)
    
    engine = AIWritingEngine()
    
    # 测试文章生成
    print("\n【文章生成】")
    article = engine.generate_article('人工智能', style='tech', length='short')
    print(f"标题: {article['title']}")
    print(f"字数: {article['word_count']}")
    print(f"内容:\n{article['content'][:200]}...")
    
    # 测试文案生成
    print("\n【营销文案生成】")
    copy = engine.generate_copy('智能手表', benefit='健康', percent='80')
    print(f"标题: {copy['title']}")
    print(f"内容:\n{copy['content']}")
    
    # 测试诗歌生成
    print("\n【诗歌生成】")
    poetry = engine.generate_poetry('秋天', style='modern')
    print(f"标题: {poetry['title']}")
    print(f"内容:\n{poetry['content']}")
