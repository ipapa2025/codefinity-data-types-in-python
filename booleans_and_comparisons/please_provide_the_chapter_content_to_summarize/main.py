age = 17
adult_age = 21
has_id = True
is_member = False

purchase_total = 120.0
free_shipping_threshold = 100.0

email_verified = True
phone_verified = False

score = 74
min_score = 0
max_score = 100

# 1) Adult check
is_adult = age ___ adult_age

# 2) Entry rule
can_enter = is_adult ___ has_id

# 3) Free shipping rule
qualifies_free_shipping = (purchase_total ___ free_shipping_threshold) ___ is_member

# 4) Manual review rule
needs_manual_review = (___ email_verified) ___ (___ phone_verified)

# 5) Score range rule
valid_score_range = min_score ___ score ___ max_score

print(is_adult, can_enter, qualifies_free_shipping, needs_manual_review, valid_score_range)