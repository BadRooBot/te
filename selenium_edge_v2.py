import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time
import json
myWordTestList=['Abo Sherif']
myWordList = ['apple', 'banana', 'orange', 'grape', 'kiwi',
    'dog', 'cat', 'rabbit', 'elephant', 'giraffe',
    'sun', 'moon', 'star', 'planet', 'galaxy',
    'happy', 'sad', 'excited', 'calm', 'surprised',
    'book', 'pen', 'paper', 'computer', 'notebook',
    'mountain', 'river', 'ocean', 'desert', 'forest',
    'red', 'blue', 'green', 'yellow', 'purple',
    'fast', 'slow', 'high', 'low', 'medium',
    'family', 'friend', 'love', 'hate', 'trust',
    'car', 'bicycle', 'train', 'airplane', 'boat',
    'music', 'art', 'dance', 'poetry', 'film',
    'delicious', 'spicy', 'sweet', 'sour', 'bitter',
    'time', 'space', 'energy', 'matter', 'gravity',
    'laughter', 'tears', 'smile', 'frown', 'grin',
    'hope', 'faith', 'dream', 'reality', 'illusion',
    'computer', 'keyboard', 'mouse', 'monitor', 'printer',
    'school', 'teacher', 'student', 'classroom', 'education',
    'courage', 'fear', 'strength', 'weakness', 'bravery',
    'victory', 'defeat', 'success', 'failure', 'achievement',
    'imagination', 'creativity', 'innovation', 'inspiration', 'improvement',
    'friendship', 'loyalty', 'betrayal', 'forgiveness', 'trustworthiness',
    'sky', 'earth', 'fire', 'water', 'air',
    'knowledge', 'wisdom', 'intelligence', 'ignorance', 'curiosity',
    'technology', 'science', 'engineering', 'medicine', 'communication',
    'justice', 'equality', 'freedom', 'peace', 'security',
    'happiness', 'sadness', 'anger', 'fear', 'disgust',
    'space', 'time', 'infinity', 'eternity', 'dimension',
    'robot', 'android', 'cyborg', 'AI', 'virtual',
    'algorithm', 'code', 'program', 'data', 'information',
    'ancient', 'modern', 'future', 'past', 'present',
    'spirit', 'soul', 'mind', 'body', 'consciousness',
    'challenge', 'obstacle', 'opportunity', 'adventure', 'risk',
    'explore', 'discover', 'learn', 'grow', 'evolve',
    'health', 'wellness', 'fitness', 'nutrition', 'exercise',
    'meditation', 'reflection', 'introspection', 'mindfulness', 'awareness',
    'vision', 'mission', 'goal', 'objective', 'purpose',
    'faithful', 'trustworthy', 'reliable', 'dependable', 'consistent',
    'celebrate', 'commemorate', 'memorialize', 'acknowledge', 'recognize',
    'overcome', 'persevere', 'endure', 'triumph', 'prevail',
    'inspire', 'motivate', 'encourage', 'uplift', 'empower',
    'perseverance', 'determination', 'resilience', 'tenacity', 'fortitude',
    'effort', 'commitment', 'dedication', 'discipline', 'persistence',
    'random', 'chaotic', 'ordered', 'structured', 'systematic',
    'language', 'communication', 'expression', 'speech', 'dialogue',
    'connect', 'communicate', 'interact', 'relate', 'engage',
    'adventure', 'explore', 'discover', 'journey', 'experience',
    'harmony', 'balance', 'unity', 'diversity', 'variety',
    'observe', 'perceive', 'experience', 'understand', 'comprehend',
    'unity', 'diversity', 'variety', 'complexity', 'simplicity',
    'efficiency', 'effectiveness', 'optimization', 'improvement', 'streamline',
    'community', 'society', 'culture', 'tradition', 'heritage',
    'sunrise', 'sunset', 'twilight', 'dawn', 'dusk',
    'harvest', 'plow', 'plant', 'nurture', 'cultivate',
    'abundance', 'scarcity', 'plenty', 'dearth', 'wealth',
    'journey', 'destination', 'path', 'road', 'trail',
    'abundant', 'bountiful', 'plentiful', 'copious', 'generous',
    'endless', 'limitless', 'boundless', 'infinite', 'eternal',
    'beginning', 'middle', 'end', 'start', 'finish',
    'build', 'create', 'construct', 'develop', 'form',
    'obstacle', 'challenge', 'hurdle', 'barrier', 'difficulty',
    'joy', 'happiness', 'glee', 'contentment', 'satisfaction',
    'knowledge', 'wisdom', 'understanding', 'insight', 'awareness',
    'compassion', 'empathy', 'kindness', 'generosity', 'charity',
    'flexible', 'adaptable', 'resilient', 'versatile', 'pliable',
    'connectivity', 'network', 'link', 'tie', 'relationship',
    'contemplate', 'meditate', 'reflect', 'ponder', 'consider',
    'imagine', 'dream', 'envision', 'fantasize', 'conceive',
    'vibrant', 'dynamic', 'lively', 'energetic', 'animated',
    'serene', 'calm', 'tranquil', 'peaceful', 'soothing',
    'courage', 'bravery', 'valor', 'fearlessness', 'daring',
    'resolute', 'determined', 'steadfast', 'unyielding', 'persistent',
    'innovate', 'invent', 'create', 'devise', 'originate',
    'nourish', 'nurture', 'foster', 'cultivate', 'develop',
    'observe', 'examine', 'scrutinize', 'inspect', 'survey',
    'improve', 'enhance', 'upgrade', 'amplify', 'augment',
    'acknowledge', 'recognize', 'appreciate', 'admit', 'confess',
    'understand', 'comprehend', 'grasp', 'fathom', 'realize',
    'inspire', 'motivate', 'encourage', 'uplift', 'stimulate',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'recognize',
    'heal', 'recover', 'restore', 'rejuvenate', 'revitalize',
    'ascend', 'transcend', 'elevate', 'rise', 'climb',
    'embrace', 'accept', 'welcome', 'adopt', 'incorporate',
    'forgive', 'pardon', 'absolve', 'excuse', 'remission',
    'cherish', 'treasure', 'value', 'appreciate', 'admire',
    'laugh', 'smile', 'giggle', 'chuckle', 'grin',
    'explore', 'discover', 'investigate', 'research', 'examine',
    'dream', 'fantasize', 'imagine', 'envision', 'conceive',
    'illuminate', 'enlighten', 'brighten', 'clarify', 'shine',
    'adapt', 'adjust', 'modify', 'alter', 'change',
    'achieve', 'accomplish', 'attain', 'reach', 'realize',
    'create', 'innovate', 'generate', 'originate', 'produce',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'connect', 'link', 'unite', 'join', 'combine',
    'explore', 'investigate', 'examine', 'research', 'study',
    'communicate', 'convey', 'express', 'share', 'converse',
    'meditate', 'contemplate', 'reflect', 'ponder', 'consider',
    'love', 'compassion', 'empathy', 'kindness', 'generosity',
    'harmony', 'balance', 'peace', 'unity', 'tranquility',
    'explore', 'adventure', 'discover', 'journey', 'experience',
    'appreciate', 'admire', 'value', 'cherish', 'treasure',
    'persevere', 'persist', 'endure', 'overcome', 'triumph',
    'learn', 'educate', 'enlighten', 'inform', 'teach',
    'improve', 'enhance', 'grow', 'develop', 'evolve',
    'create', 'innovate', 'design', 'build', 'construct',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'remember',
    'smile', 'laugh', 'giggle', 'chuckle', 'grin',
    'listen', 'hear', 'pay attention', 'understand', 'comprehend',
    'dream', 'fantasize', 'imagine', 'envision', 'conceive',
    'forgive', 'pardon', 'excuse', 'absolve', 'remission',
    'imagine', 'dream', 'envision', 'fantasize', 'conceive',
    'explore', 'discover', 'investigate', 'research', 'examine',
    'appreciate', 'admire', 'value', 'cherish', 'treasure',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'remember',
    'improve', 'enhance', 'upgrade', 'amplify', 'augment',
    'adapt', 'adjust', 'modify', 'alter', 'change',
    'connect', 'link', 'unite', 'join', 'combine',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'persevere', 'persist', 'endure', 'overcome', 'triumph',
    'create', 'innovate', 'generate', 'originate', 'produce',
    'love', 'compassion', 'empathy', 'kindness', 'generosity',
    'harmony', 'balance', 'peace', 'unity', 'tranquility',
    'explore', 'adventure', 'discover', 'journey', 'experience',
    'appreciate', 'admire', 'value', 'cherish', 'treasure',
    'persevere', 'persist', 'endure', 'overcome', 'triumph',
    'learn', 'educate', 'enlighten', 'inform', 'teach',
    'improve', 'enhance', 'grow', 'develop', 'evolve',
    'create', 'innovate', 'design', 'build', 'construct',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'remember',
    'smile', 'laugh', 'giggle', 'chuckle', 'grin',
    'listen', 'hear', 'pay attention', 'understand', 'comprehend',
    'dream', 'fantasize', 'imagine', 'envision', 'conceive',
    'forgive', 'pardon', 'excuse', 'absolve', 'remission',
    'imagine', 'dream', 'envision', 'fantasize', 'conceive',
    'explore', 'discover', 'investigate', 'research', 'examine',
    'appreciate', 'admire', 'value', 'cherish', 'treasure',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'remember',
    'improve', 'enhance', 'upgrade', 'amplify', 'augment',
    'adapt', 'adjust', 'modify', 'alter', 'change',
    'connect', 'link', 'unite', 'join', 'combine',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'persevere', 'persist', 'endure', 'overcome', 'triumph',
    'create', 'innovate', 'generate', 'originate', 'produce',
    'love', 'compassion', 'empathy', 'kindness', 'generosity',
    'harmony', 'balance', 'peace', 'unity', 'tranquility',
    'explore', 'adventure', 'discover', 'journey', 'experience',
    'appreciate', 'admire', 'value', 'cherish', 'treasure',
    'persevere', 'persist', 'endure', 'overcome', 'triumph',
    'learn', 'educate', 'enlighten', 'inform', 'teach',
    'improve', 'enhance', 'grow', 'develop', 'evolve',
    'create', 'innovate', 'design', 'build', 'construct',
    'inspire', 'motivate', 'encourage', 'uplift', 'ignite',
    'celebrate', 'commemorate', 'memorialize', 'honor', 'remember',
    'smile', 'laugh','apple', 'happy', 'sun', 'blue', 'ocean', 'book', 'run', 'cat', 'dog', 'tree', 'mountain', 'cloud', 'guitar', 'joy', 'jump', 'hope', 'love', 'peace', 'smile', 'wind', 'moon', 'star', 'fire', 'water', 'time', 'space', 'science', 'technology', 'innovation', 'music', 'art', 'history', 'culture', 'travel', 'adventure', 'explore', 'friendship', 'family', 'health', 'fitness', 'happiness', 'success', 'faith', 'kindness', 'charity', 'forgiveness', 'gratitude', 'patience', 'wisdom', 'knowledge', 'learning', 'education', 'inspiration', 'motivation', 'creativity', 'imagination', 'dream', 'passion', 'purpose', 'achievement', 'challenge', 'perseverance', 'effort', 'victory', 'celebrate', 'freedom', 'justice', 'equality', 'peaceful', 'harmony', 'nature', 'environment', 'green', 'sustainable', 'beauty', 'serenity', 'tranquility', 'meditation', 'mindfulness', 'yoga', 'laughter', 'joyful', 'festive', 'colorful', 'playful', 'vibrant', 'delicious', 'tasty', 'cuisine', 'culinary', 'fashion', 'style', 'trend', 'design', 'architecture', 'luxury', 'simplicity', 'elegance', 'modesty', 'grace', 'class', 'history', 'past', 'present', 'future', 'ancient', 'modern', 'space', 'galaxy', 'planet', 'astronomy', 'cosmos', 'universe', 'rocket', 'exploration', 'discovery', 'adventure', 'journey', 'quest', 'challenge', 'destination', 'path', 'trail', 'route', 'way', 'road', 'street', 'avenue', 'boulevard', 'alley', 'park', 'garden', 'forest', 'jungle', 'wilderness', 'desert', 'oasis', 'island', 'mountain', 'valley', 'hill', 'peak', 'canyon', 'river', 'lake', 'ocean', 'sea', 'beach', 'shore', 'coast', 'island', 'peninsula', 'cove', 'bay', 'harbor', 'port', 'village', 'town', 'city', 'metropolis', 'capital', 'nation', 'country', 'continent', 'world', 'globe', 'earth', 'solar', 'sun', 'moon', 'star', 'planet', 'galaxy', 'nebula', 'cosmos', 'universe', 'astronomy', 'physics', 'chemistry', 'biology', 'geology', 'meteorology', 'ecology', 'environment', 'climate', 'oxygen', 'carbon', 'hydrogen', 'nitrogen', 'atoms', 'molecules', 'cells', 'organs', 'species', 'evolution', 'genetics', 'mutation', 'adaptation', 'ecosystem', 'biodiversity', 'ecology', 'conservation', 'sustainability', 'renewable', 'energy', 'climate', 'change', 'pollution', 'deforestation', 'recycle', 'reuse', 'reduce', 'solar', 'wind', 'hydro', 'geothermal', 'nuclear', 'technology', 'innovation', 'invention', 'discovery', 'research', 'development', 'engineering', 'computer', 'software', 'hardware', 'internet', 'social', 'media', 'network', 'communication', 'smartphone', 'tablet', 'laptop', 'gaming', 'virtual', 'augmented', 'reality', 'cybersecurity', 'privacy', 'encryption', 'algorithm', 'coding', 'programming', 'digital', 'analog', 'algorithm', 'data', 'database', 'information', 'knowledge', 'wisdom', 'learning', 'education', 'school', 'college', 'university', 'classroom', 'lecture', 'teacher', 'student', 'exam', 'homework', 'study', 'research', 'thesis', 'dissertation', 'project', 'science', 'mathematics', 'physics', 'chemistry', 'biology', 'geology', 'history', 'literature', 'language', 'linguistics', 'philosophy', 'psychology', 'sociology', 'economics', 'politics', 'government', 'law', 'justice', 'ethics', 'morality', 'humanity', 'society', 'culture', 'tradition', 'custom', 'ceremony', 'celebration', 'ritual', 'festivity', 'holiday', 'occasion', 'event', 'party', 'wedding', 'birthday', 'anniversary', 'graduation', 'achievement', 'success', 'accomplishment', 'challenge', 'goal', 'dream', 'passion', 'desire', 'ambition', 'motivation', 'inspiration', 'creativity', 'innovation', 'art', 'music', 'literature', 'film', 'dance', 'theater', 'craft', 'sculpture', 'painting', 'drawing', 'photography', 'design', 'fashion', 'style', 'trend', 'architecture', 'engineering', 'technology', 'business', 'economics', 'finance', 'investment', 'management', 'leadership', 'entrepreneurship', 'startup', 'marketing', 'advertising', 'sales', 'customer', 'service', 'productivity', 'efficiency', 'quality', 'customer', 'satisfaction', 'teamwork', 'communication', 'collaboration', 'partnership', 'relationship', 'trust', 'integrity', 'ethics', 'values', 'responsibility', 'accountability', 'professionalism', 'work', 'career', 'job', 'employment', 'office', 'workplace', 'colleague', 'boss', 'employee', 'salary', 'benefit', 'promotion', 'growth', 'challenge', 'opportunity', 'change', 'adaptation', 'learning', 'development', 'success', 'failure', 'experience', 'wisdom', 'knowledge', 'health', 'wellness', 'fitness', 'exercise', 'nutrition', 'mental', 'emotional', 'spiritual', 'well-being', 'mindfulness', 'meditation', 'yoga', 'relaxation', 'stress', 'anxiety', 'depression', 'therapy', 'counseling', 'support', 'friendship', 'family', 'relationship', 'communication', 'love', 'trust', 'loyalty', 'forgiveness', 'compassion', 'empathy', 'kindness', 'generosity', 'gratitude', 'integrity', 'character', 'personality', 'attitude', 'behavior', 'habit', 'routine', 'discipline', 'perseverance', 'dedication', 'patience', 'resilience', 'optimism', 'positivity', 'success', 'achievement', 'accomplishment', 'goal', 'dream', 'passion', 'purpose', 'fulfillment', 'happiness', 'joy', 'satisfaction', 'celebration', 'victory', 'reward', 'recognition', 'appreciation', 'gratitude', 'thanks', 'smile', 'laughter', 'fun', 'play', 'recreation', 'hobby', 'interest', 'entertainment', 'adventure', 'travel', 'exploration', 'discovery', 'curiosity', 'wonder', 'awe', 'beauty', 'artistry', 'creativity', 'imagination', 'expression', 'communication', 'inspiration', 'motivation', 'growth', 'learning', 'education', 'knowledge', 'wisdom', 'understanding', 'awareness', 'consciousness', 'mindfulness', 'spirituality', 'connection', 'meaning', 'purpose', 'fulfillment', 'peace', 'joy', 'happiness', 'love', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'creativity', 'innovation', 'imagination', 'play', 'fun', 'adventure', 'curiosity', 'wonder', 'awe', 'beauty', 'expression', 'communication', 'connection', 'relationship', 'community', 'collaboration', 'cooperation', 'support', 'empathy', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'purpose', 'fulfillment', 'meaning', 'joy', 'happiness', 'love', 'appreciation', 'gratitude', 'thanks', 'smile', 'laughter', 'fun', 'play', 'recreation', 'hobby', 'interest', 'entertainment', 'adventure', 'travel', 'exploration', 'discovery', 'curiosity', 'wonder', 'awe', 'beauty', 'artistry', 'creativity', 'imagination', 'expression', 'communication', 'inspiration', 'motivation', 'growth', 'learning', 'education', 'knowledge', 'wisdom', 'understanding', 'awareness', 'consciousness', 'mindfulness', 'spirituality', 'connection', 'meaning', 'purpose', 'fulfillment', 'peace', 'joy', 'happiness', 'love', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'creativity', 'innovation', 'imagination', 'play', 'fun', 'adventure', 'curiosity', 'wonder', 'awe', 'beauty', 'expression', 'communication', 'connection', 'relationship', 'community', 'collaboration', 'cooperation', 'support', 'empathy', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'purpose', 'fulfillment', 'meaning', 'joy', 'happiness', 'love', 'appreciation', 'gratitude', 'thanks', 'smile', 'laughter', 'fun', 'play', 'recreation', 'hobby', 'interest', 'entertainment', 'adventure', 'travel', 'exploration', 'discovery', 'curiosity', 'wonder', 'awe', 'beauty', 'artistry', 'creativity', 'imagination', 'expression', 'communication', 'inspiration', 'motivation', 'growth', 'learning', 'education', 'knowledge', 'wisdom', 'understanding', 'awareness', 'consciousness', 'mindfulness', 'spirituality', 'connection', 'meaning', 'purpose', 'fulfillment', 'peace', 'joy', 'happiness', 'love', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'creativity', 'innovation', 'imagination', 'play', 'fun', 'adventure', 'curiosity', 'wonder', 'awe', 'beauty', 'expression', 'communication', 'connection', 'relationship', 'community', 'collaboration', 'cooperation', 'support', 'empathy', 'compassion', 'kindness', 'gratitude', 'forgiveness', 'hope', 'optimism', 'faith', 'trust', 'courage', 'strength', 'resilience', 'perseverance', 'patience', 'discipline', 'balance', 'harmony', 'wholeness', 'well-being', 'health', 'vitality', 'energy', 'enthusiasm', 'passion', 'purpose', 'fulfillment', 'meaning', 'joy', 'happiness', 'love', 'appreciation', 'gratitude', 'thanks', 'smile', 'laughter', 'fun', 'play', 'recreation', 'hobby', 'interest', 'entertainment', 'adventure', 'travel', 'exploration', 'discovery', 'curiosity', 'wonder', 'awe', 'beauty', 'artistry', 'creativity', 'imagination', 'expression', 'communication', 'inspiration', 'motivation', 'growth', 'learning', 'education', 'knowledge', 'wisdom', 'understanding', 'awareness', 'consciousness', 'mindfulness', 'spirituality', 'connection', 'meaning', 'purpose', 'fulfillment','Actions speak louder than words.', 'All that glitters is not gold.', 'Better late than never.', 'Birds of a feather flock together.', 'Bite the bullet.', 'Break the ice.', 'Burning the midnight oil.', 'Cry over spilled milk.', 'Curiosity killed the cat.', 'Don’t count your chickens before they hatch.',
'العقل زينة.', 'اللبيب من الأطباء.', 'أحسن الظن بالناس.', 'أذن من رأس.', 'إذا ذل الإنسان ابتلى.', 'الجار قبل الدار.', 'الحاجة أم الاختراع.', 'الحرف بالمحبة يصغر.', 'الصديق وقت الضيق.', 'الطيور على أشكالها تقع.',
'A penny for your thoughts.', 'Actions speak louder than words.', 'An apple a day keeps the doctor away.', 'Bite off more than you can chew.', 'Burning the midnight oil.', 'Don''t put all your eggs in one basket.', 'Every cloud has a silver lining.', 'Give someone the cold shoulder.', 'Hit the nail on the head.', 'Ignorance is bliss.',
'إن أفضل الكتب هو كتاب الله.', 'إنما العلم بالتعلم.', 'الإحسان إلى الكل خير.', 'الاستماع خير من الكلام.', 'البطيخة من بيت أبوها.', 'الحب أعمى.', 'الحمد لله على كل حال.', 'الخبز على الماء.', 'الدنيا دار ضياع.', 'الراحة في الدنيا تكون في القلب.',
'Every dog has its day.', 'Give the devil his due.', 'Hit the hay.', 'In the heat of the moment.', 'It takes two to tango.', 'Let bygones be bygones.', 'Make hay while the sun shines.', 'Out of the frying pan and into the fire.', 'Put all your eggs in one basket.', 'Rome wasn''t built in a day.',
'الرجاء الدخول بدون حذاء.', 'السكوت علامة الرضا.', 'الشجاعة هي الرجولة.', 'الصديق وقت الضيق.', 'العبرة بالأخلاق.', 'الغريب يرحب بك الله.', 'الفاعل يفعل والساكت شارك.', 'القرد في عين أمه غزال.', 'الكرامة خير من المال.', 'الله لا يضيع أجر المحسنين.',
'The early bird catches the worm.', 'The grass is always greener on the other side.', 'The pot calling the kettle black.', 'To kill two birds with one stone.', 'Two heads are better than one.', 'When in Rome, do as the Romans do.', 'You can''t have your cake and eat it too.', 'You can''t make an omelet without breaking eggs.', 'You reap what you sow.', 'Your guess is as good as mine.',
'إذا كنت تعمل، فأنت تفشل أحيانًا.', 'إن العقل زينة.', 'الأمل آخر الليل.', 'الحب أعمى.', 'العشق يبدأ بالنظرة.', 'العقل زينة.', 'الغاية تبرر الوسيلة.', 'القلب يحكم.', 'الكلمة الطيبة صدقة.', 'الناس سواسية كأسنان المشط.',
'You''ve bitten off more than you can chew.', 'A picture is worth a thousand words.', 'A watched pot never boils.', 'Actions speak louder than words.', 'All good things must come to an end.', 'An ounce of prevention is worth a pound of cure.', 'Bite the bullet.', 'Burning the midnight oil.', 'Don''t put all your eggs in one basket.', 'Every cloud has a silver lining.',
'أقلها ثلاث مرات.', 'أنا رجل صالح.', 'باب الفرج مفتوح.', 'بالعافية والهناء.', 'تحت السيطرة.', 'تسلم الأيادي.', 'ثابر وتوكل.', 'جزاك الله خيراً.', 'حب الوطن من الإيمان.', 'حبة خير من ألف علم.', 'أقول قولاً فأنا به.',
'Every man for himself.', 'Fortune favors the bold.', 'Good things come to those who wait.', 'If the shoe fits, wear it.', 'It''s a piece of cake.', 'Jump on the bandwagon.', 'Kill two birds with one stone.', 'Let the cat out of the bag.', 'Make a long story short.', 'No pain, no gain.',
'سامح تؤجر.', 'شر البلية ما يضحك.', 'صارت الحديثة معروفة.', 'على قدر لحافك مد رجليك.', 'كلما زادت الخرابيش زاد الربح.', 'لكل جواد كبوة.', 'من شب على شيء شاب عليه.', 'نصف السعادة في العلم.', 'همتك فوق همتك.', 'وقع الإنسان في الخطأ.',
'No pain, no gain.', 'Once bitten, twice shy.','Quote of the day', 'Venice', 'bestegytech', 'mohamed salah', 'socrates', 'dinner recipes',
         'Bing Homepage quiz', 'RobbergReserveSouthAfrica', "How to make a cake",
        "Best movies of 2021",
        "What is the meaning of life",
        "Who is the president of France",
        "When will the pandemic end",
        "Where can I buy a cheap laptop",
        "Why do cats purr",
        "How to play chess",
        "Best books of 2020",
        "What is the weather in London",
        "Who invented the internet",
        "When is the next solar eclipse",
        "Where is the Eiffel Tower",
        "Why do we dream",
        "How to meditate",
        "Best podcasts of 2021",
        "What is the capital of Brazil",
        "Who won the Oscars in 2020",
        "When is the best time to visit Japan",
        "Where can I learn a new language",
        "Why do we yawn",
        "How to write a resume",
        "Best games of 2020",
        "What is the fastest animal in the world",
        "Who is the richest person in the world",
        "When is the next Olympics",
        "Where can I watch free movies online",
        "Why do we sneeze",
        "How to draw a face",
        "Best songs of 2023"]


driver = None  # Initialize the driver variable outside the try block
homePage = 'https://www.bing.com/search?pglt=163&PC=U523&q=bestegytech&FORM=ANAB01'
searchPage = 'https://www.bing.com/'
profilePage='edge://settings/profiles'
loginCardViewUrl='edge://edge-customized-hrd'
waitTime = 4
longWaitTime = 5
shortTime=1
print('B A D R O O B O T ======================================================================================================================================================')

def resource_path(relative_path: str) -> str:
    """
    Get the absolute path of a file or resource, regardless of whether the code is running from a source distribution or from the original source files.

    Args:
        relative_path: The relative path of the file or resource.

    Returns:
        The absolute path of the file or resource.
    """
    try:
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:

    # Set the path to the Microsoft Edge WebDriver executable
    driver_path = resource_path("edge_driver\msedgedriver.exe")

    # Create the driver service object
    driver_service = Service(executable_path=driver_path)
    driver_options = Options()
    options = Options()
    # options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    # # An example of option you can use:
    # # this is something I used to disable warning messages about not logging in.
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Create the driver object
    driver = webdriver.Edge(service=driver_service,options=driver_options)

    # Navigate to the search page
    driver.get(searchPage)

    # Wait for the page title to contain "Bing"
    WebDriverWait(driver, longWaitTime).until(EC.title_contains("Bing"))

    # Find the search field element by its name attribute
    search_field = driver.find_element(By.NAME, "q")

    # Enter the search query "bestegytech" into the search field
    search_field.send_keys("bestegytech")

    # Submit the search query
    search_field.submit()

    def random_selection(my_list, k):
        # If the length of the list is less than k
        if len(my_list) < k:
            return "Error: the length of the list is less than k."
        
        # If k equals to 0
        if k == 0:
            return []
        
        # Create a copy of the original list
        copy_list = my_list[:]
        
        # Initialize an empty list to store the selected items
        selected_items = []
        
        # Iterate k times
        for i in range(k):
            # Generate a random index within the range of the current length of the list
            random_index = random.randint(0, len(copy_list) - 1)
            
            # Append the selected item to the selected items list
            selected_items.append(copy_list[random_index])
            
            # Remove the selected item from the copy list
            copy_list.pop(random_index)
        
        return selected_items

    # Test the function with a list of 100 items and selecting 30 items
    my_list = list(range(100))
    k = 32
    search_word=random_selection(myWordList, k)
    def search_handler():
        for word in myWordTestList:
                    print('search_handler received')
                    time.sleep(3)
                    search_field = driver.find_elements(By.NAME, "q")
                    if search_field:   
                        print('search_field',search_field[0].tag_name)
                        time.sleep(shortTime)
                        search_field[0].clear()
                        time.sleep(shortTime)
                        search_field[0].send_keys(word)
                        print('word sending',word)
                        time.sleep(shortTime)
                        search_field[0].submit()
                        print('word submitted',word)
                        time.sleep(3)
        signOut_handler(False)                           
    # Find the Sing in button element by its id =id_l
    def signOut_handler(is_first_time):
            print ("Already logged in. logout started")
            sign_out_button=driver.find_elements(By.ID,'currentProfileCardActionButton')
            if sign_out_button:
                sign_out_button[0].click()
                time.sleep(3)
                clear_history_checbox=driver.find_elements(By.ID,'settings-checkbox-input-74')
                if clear_history_checbox:
                    clear_history_checbox[0].click()
                    time.sleep(2)
                    confirm_sign_out_button=driver.find_elements(By.ID,'confirmModalPrimaryButton')
                    if confirm_sign_out_button:
                        confirm_sign_out_button[0].click()
    def login_handler():
        usersJson='users.json'
        with open(usersJson, 'r') as f:
                users = json.load(f)
        if users:
            print('All Email  = ', users['all'])
        time.sleep(waitTime)
        signIn=driver.find_elements(By.ID,"sign-in-button")
        print('signIn is click done')       
        if signIn:
            rg=len(users['all'])
            signIn[0].click()
            for oneUser in users['all']:
                    time.sleep(2.5)
                    print('Selected Email',oneUser)
                    print('Email count',rg)
                    addNewEmail=driver.find_elements(By.ID,"id_a")
                    
                    # time.sleep(waitTime)
                    # signIn[0].click()
                    time.sleep(waitTime)
                    email_field = driver.find_elements(By.ID, "i0116")
                    if email_field:
                        email_field.send_keys(oneUser['email'])
                        time.sleep(shortTime)
                        driver.find_element(By.ID, "idSIButton9").click()
                        time.sleep(waitTime)
                        password_field = driver.find_element(By.ID, "i0118")
                        password_field.send_keys(oneUser['password'])
                        time.sleep(shortTime)
                        driver.find_element(By.ID, "idSIButton9").click()
                        time.sleep(waitTime)
                        try:
                            btnBack= driver.find_elements(By.ID, "declineButton")
                            if btnBack:
                                btnBack[0].click()
                            else:
                                btnYes= driver.find_elements(By.ID, "acceptButton")
                                if btnYes:
                                    btnYes[0].click()    
                        except Exception as e:
                            print(f"An error occurred: {str(e)}")
                        time.sleep(waitTime)
                        driver.get(homePage)
                        time.sleep(waitTime)
                        signIn=driver.find_elements(By.ID,"id_a")
                        if signIn:
                            time.sleep(shortTime)
                            signIn[0].click()
                            time.sleep(waitTime)
                            emaillBox=driver.find_elements(By.ID,'EmailAddress')
                            time.sleep(waitTime)
                            if emaillBox:
                                driver.get("https://mail.tm/en/")
                                time.sleep(waitTime)
                                getMaill=driver.find_element(By.ID,'accounts-menu')
                                time.sleep(shortTime)
                                getMaill.click()
                                time.sleep(shortTime)
                                accountList=driver.find_element(By.ID,'accounts-list')
                                time.sleep(shortTime)
                                accountList.find_elements(By.TAG_NAME,'p')
                                time.sleep(shortTime)
                                print('acc   =====   ',accountList.text.split('\n'))
                                tempMail=accountList.text.split('\n')[1]
                                print(tempMail)
                                time.sleep(shortTime)
                                driver.back()
                                time.sleep(5)
                                driver.refresh()
                                time.sleep(waitTime)
                                emaillBox=driver.find_elements(By.ID,'EmailAddress')
                                time.sleep(1)
                                emaillBox[0].send_keys(tempMail)
                                time.sleep(2)
                                nextBtn=driver.find_element(By.ID,'iNext')
                                time.sleep(1)
                                nextBtn.click()
                                time.sleep(2)
                                driver.get('https://mail.tm/en/')
                                time.sleep(waitTime)
                                new_message=driver.find_elements(By.TAG_NAME,'li')
                                time.sleep(shortTime)
                                new_message[0].click()
                                time.sleep(waitTime)
                                frame = driver.find_element(By.ID, "iFrameResizer0")
                                time.sleep(waitTime)
                                driver.switch_to.frame(frame)
                                print('tr =====================   switch to done')
                                time.sleep(waitTime)
                                bodyText=driver.find_elements(By.ID,'i4')
                                print('tr =====================   ',bodyText)
                                time.sleep(shortTime)
                                security_code = bodyText[0].find_elements(By.TAG_NAME,'span')
                                time.sleep(shortTime)
                                security_code=security_code[0].text
                                time.sleep(waitTime)
                                driver.back()
                                time.sleep(waitTime)
                                driver.back()
                                time.sleep(waitTime)
                                codeBox=driver.find_element(By.NAME,'iOttText')
                                time.sleep(shortTime)
                                codeBox.send_keys(security_code)
                                time.sleep(shortTime)
                                driver.find_element(By.ID,'iNext').click()
                    time.sleep(waitTime)
                    driver.get(searchPage)
                    search_handler()    

                    
                
        else:
            driver.get(searchPage)
            time.sleep(waitTime)
            check_if_signed_in()

    def check_if_signed_in ():
        sign_in_button= driver.find_elements(By.ID,'sign-in-button')
        time.sleep(shortTime)
        if  sign_in_button:
            login_handler()      
        else:
            sign_out_button=driver.find_elements(By.ID,'currentProfileCardActionButton')
            print('Start sign out')
            time.sleep(waitTime)
            if sign_out_button:
                signOut_handler(True)
 
        
    # Sleep for waitTime seconds
    driver.get(profilePage)
    time.sleep(waitTime)
    check_if_signed_in()        
    time.sleep(waitTime)  
    print('كل حاجه تمام تم البحث بنجاح  -__-  صلي علي النبي ') 
    if driver:
        driver.quit() 
except Exception as e:
    # Print the error message if an exception occurs
    print("Error occurred: HOME ERROR  ", e)
    
    # Quit the driver if it exists
    if driver:
        driver.quit()

while True:
    pass
