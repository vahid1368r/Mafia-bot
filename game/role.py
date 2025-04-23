# تعریف نقش‌ها و توضیحاتشان
ROLES = {
    "classic":      ["mafia","doctor","detective","villager"],
    "advanced":     ["mafia","doctor","detective","villager","guardian","inquisitor"],
    "army":         ["mafia","doctor","detective","commander","soldier"],
    "godfather":    ["mafia","doctor","detective","godfather"],
    "zodiac":       ["mafia","doctor","detective","zodiac"],
    "croupier":     ["mafia","doctor","detective","croupier"],
}
ROLE_DESC = {
    "mafia":      "هر شب مافیا تصمیم می‌گیرد یک نفر را حذف کند.",  
    "doctor":     "هر شب می‌تواند یک نفر را نجات دهد.",  
    "detective":  "هر شب می‌تواند نقش یک نفر را بررسی کند.",  
    "villager":   "فقط در روز رای می‌دهد و سعی می‌کند مافیا را پیدا کند.",  
    "guardian":   "می‌تواند در شب از یک نفر محافظت کند.",  
    "inquisitor":"در شب تشخیص می‌دهد که آیا یک نفر مافیا است یا نه.",  
    "commander": "فرمانده ارتش؛ دستور ویژه در شب ارسال می‌کند.",  
    "soldier":    "سرباز معمولی ارتش.",  
    "godfather":  "رهبر مافیا؛ رای نهایی کشتن را صادر می‌کند.",  
    "zodiac":     "در شب به‌طور تصادفی یک نفر را حذف می‌کند.",  
    "croupier":   "قمارباز؛ در شب شانس حذف تصادفی را امتحان می‌کند.",  
}