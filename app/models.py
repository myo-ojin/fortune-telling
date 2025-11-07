"""
Database models for the Fortune Telling application.
"""
from datetime import datetime
from app.database import db


class FortuneMethod(db.Model):
    """Fortune telling method master table"""
    __tablename__ = 'fortune_methods'

    id = db.Column(db.Integer, primary_key=True)
    name_ja = db.Column(db.String(100), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FortuneMethod {self.name_ja}>'


class ZodiacSign(db.Model):
    """12 Zodiac signs table"""
    __tablename__ = 'zodiac_signs'

    id = db.Column(db.Integer, primary_key=True)
    name_ja = db.Column(db.String(50), nullable=False)
    name_en = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10))
    element = db.Column(db.String(20))
    quality = db.Column(db.String(20))
    ruling_planet = db.Column(db.String(50))
    date_range_start = db.Column(db.String(10))
    date_range_end = db.Column(db.String(10))
    love_trait = db.Column(db.Text)
    work_trait = db.Column(db.Text)
    health_trait = db.Column(db.Text)
    money_trait = db.Column(db.Text)

    def __repr__(self):
        return f'<ZodiacSign {self.name_ja}>'


class TarotCard(db.Model):
    """Tarot cards table (Major Arcana only)"""
    __tablename__ = 'tarot_cards'

    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer, nullable=False)
    name_ja = db.Column(db.String(50), nullable=False)
    name_en = db.Column(db.String(50), nullable=False)
    arcana_type = db.Column(db.String(20), nullable=False, default='major')
    upright_general = db.Column(db.Text)
    upright_love = db.Column(db.Text)
    upright_work = db.Column(db.Text)
    upright_health = db.Column(db.Text)
    upright_money = db.Column(db.Text)
    reversed_general = db.Column(db.Text)
    reversed_love = db.Column(db.Text)
    reversed_work = db.Column(db.Text)
    reversed_health = db.Column(db.Text)
    reversed_money = db.Column(db.Text)
    keywords = db.Column(db.Text)

    def __repr__(self):
        return f'<TarotCard {self.name_ja}>'


class NumerologyMeaning(db.Model):
    """Numerology number meanings table"""
    __tablename__ = 'numerology_meanings'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    is_master_number = db.Column(db.Boolean, default=False)
    general_meaning = db.Column(db.Text)
    personality_trait = db.Column(db.Text)
    love_meaning = db.Column(db.Text)
    work_meaning = db.Column(db.Text)
    health_meaning = db.Column(db.Text)
    money_meaning = db.Column(db.Text)
    strengths = db.Column(db.Text)
    weaknesses = db.Column(db.Text)

    def __repr__(self):
        return f'<NumerologyMeaning {self.number}>'


class IChingHexagram(db.Model):
    """I Ching 64 hexagrams table"""
    __tablename__ = 'iching_hexagrams'

    id = db.Column(db.Integer, primary_key=True)
    hexagram_number = db.Column(db.Integer, nullable=False, unique=True)
    name_ja = db.Column(db.String(50), nullable=False)
    name_zh = db.Column(db.String(50))
    name_en = db.Column(db.String(100))
    symbol = db.Column(db.String(10))
    binary_code = db.Column(db.String(10))
    general_meaning = db.Column(db.Text)
    judgment_text = db.Column(db.Text)
    image_text = db.Column(db.Text)
    love_meaning = db.Column(db.Text)
    work_meaning = db.Column(db.Text)
    health_meaning = db.Column(db.Text)
    money_meaning = db.Column(db.Text)
    advice = db.Column(db.Text)

    def __repr__(self):
        return f'<IChingHexagram {self.hexagram_number}: {self.name_ja}>'


class ShichuStem(db.Model):
    """Ten Heavenly Stems table"""
    __tablename__ = 'shichu_stems'

    id = db.Column(db.Integer, primary_key=True)
    stem_name_ja = db.Column(db.String(10), nullable=False)
    stem_name_zh = db.Column(db.String(10))
    stem_name_en = db.Column(db.String(20))
    element = db.Column(db.String(10), nullable=False)
    polarity = db.Column(db.String(10), nullable=False)
    order_num = db.Column(db.Integer, nullable=False)
    general_meaning = db.Column(db.Text)
    personality_trait = db.Column(db.Text)

    def __repr__(self):
        return f'<ShichuStem {self.stem_name_ja}>'


class ShichuBranch(db.Model):
    """Twelve Earthly Branches table"""
    __tablename__ = 'shichu_branches'

    id = db.Column(db.Integer, primary_key=True)
    branch_name_ja = db.Column(db.String(10), nullable=False)
    branch_name_zh = db.Column(db.String(10))
    branch_name_en = db.Column(db.String(20))
    zodiac_animal = db.Column(db.String(20))
    element = db.Column(db.String(10), nullable=False)
    order_num = db.Column(db.Integer, nullable=False)
    month_association = db.Column(db.Integer)
    general_meaning = db.Column(db.Text)
    personality_trait = db.Column(db.Text)

    def __repr__(self):
        return f'<ShichuBranch {self.branch_name_ja}>'
