def calculate_attribute_score(attr1, attr2, weight):
    """ Helper function to calculate score for an individual attribute """
    return weight if attr1 == attr2 else 0

def calculate_interests_score(interests1, interests2, weight):
    """ Helper function to calculate score for interests """
    common_interests = set(interests1).intersection(set(interests2))
    total_interests = set(interests1).union(set(interests2))
    if total_interests:
        return (len(common_interests) / len(total_interests)) * weight
    return 0

def calculate_compatibility(user1, user2, user1_prefs, user2_prefs, weights):
    """
    Calculate compatibility between two users based on their profiles and preferences.

    :param user1: dict, profile of the first user
    :param user2: dict, profile of the second user
    :param user1_prefs: dict, preferences of the first user
    :param user2_prefs: dict, preferences of the second user
    :param weights: dict, weights for each attribute
    :return: float, compatibility percentage
    """
    # Initialize total score and weight
    total_score = 0
    total_weight = sum(weights.values())

    # Compare attributes based on user preferences
    for attr in ['gender', 'height', 'skin_complexion', 'body_type', 'hair_size', 'education', 'career', 'religion', 'description']:
        user1_score = calculate_attribute_score(user1[attr], user2_prefs[attr], weights[attr])
        user2_score = calculate_attribute_score(user2[attr], user1_prefs[attr], weights[attr])
        total_score += (user1_score + user2_score) / 2

    # Compare interests
    interests_score = calculate_interests_score(user1['interests'], user2['interests'], weights['interests'])
    total_score += interests_score

    # Calculate compatibility percentage
    compatibility_percentage = (total_score / total_weight) * 100
    return compatibility_percentage

def calculate_compatibility_for_multiple_users(main_user, main_user_prefs, other_users, other_users_prefs, weights):
    """
    Calculate compatibility between one user and multiple other users.

    :param main_user: dict, profile of the main user
    :param main_user_prefs: dict, preferences of the main user
    :param other_users: list of dicts, profiles of the other users
    :param other_users_prefs: list of dicts, preferences of the other users
    :param weights: dict, weights for each attribute
    :return: list of tuples, each containing the other user's id and the compatibility percentage
    """
    results = []
    for other_user, other_user_prefs in zip(other_users, other_users_prefs):
        # Skip users with the same gender as the main user
        if main_user['gender'] == other_user['gender']:
            continue
        compatibility = calculate_compatibility(main_user, other_user, main_user_prefs, other_user_prefs, weights)
        results.append((other_user['user_id'], compatibility))
    return results

# Example user profiles, preferences and weights
main_user = {
    'gender': 'male',
    'height': '5\'10"',
    'skin_complexion': 'fair',
    'body_type': 'athletic',
    'hair_size': 'short',
    'interests': ['music', 'reading', 'hiking'],
    'education': 'college',
    'career': 'engineer',
    'religion': 'none',
    'social_habits': 'non-smoker',
    'm_status': 'single',
    'temperament': 'calm',
    'description': 'outgoing',
    'children': 'no',
    'user_id': 1
}

main_user_prefs = {
    'gender': 'female',
    'height': '5\'6"',
    'skin_complexion': 'medium',
    'body_type': 'slim',
    'hair_size': 'long',
    'interests': ['music', 'movies', 'hiking'],
    'education': 'college',
    'career': 'teacher',
    'religion': 'christian',
    'description': 'adventurous',
    'age': 27,
    'user_id': 1
}

other_users = [
    {
        'gender': 'female',
        'height': '5\'6"',
        'skin_complexion': 'medium',
        'body_type': 'slim',
        'hair_size': 'long',
        'interests': ['music', 'movies', 'hiking'],
        'education': 'college',
        'career': 'teacher',
        'religion': 'christian',
        'social_habits': 'non-smoker',
        'm_status': 'single',
        'temperament': 'calm',
        'description': 'adventurous',
        'children': 'no',
        'user_id': 2
    },
    {
        'gender': 'female',
        'height': '5\'5"',
        'skin_complexion': 'dark',
        'body_type': 'curvy',
        'hair_size': 'short',
        'interests': ['reading', 'traveling', 'cooking'],
        'education': 'high school',
        'career': 'chef',
        'religion': 'none',
        'social_habits': 'social drinker',
        'm_status': 'single',
        'temperament': 'sanguine',
        'description': 'friendly',
        'children': 'yes',
        'user_id': 3
    }
]

other_users_prefs = [
    {
        'gender': 'male',
        'height': '5\'10"',
        'skin_complexion': 'fair',
        'body_type': 'athletic',
        'hair_size': 'short',
        'interests': ['music', 'reading', 'hiking'],
        'education': 'college',
        'career': 'engineer',
        'religion': 'none',
        'description': 'outgoing',
        'age': 25,
        'user_id': 1
    },
    {
        'gender': 'female',
        'height': '6\'0"',
        'skin_complexion': 'fair',
        'body_type': 'average',
        'hair_size': 'medium',
        'interests': ['cooking', 'traveling', 'sports'],
        'education': 'college',
        'career': 'teacher',
        'religion': 'christian',
        'description': 'adventurous',
        'age': 28,
        'user_id': 1
    }
]

weights = {
    'gender': 0.1,
    'height': 0.4,
    'skin_complexion': 0.1,
    'body_type': 0.1,
    'hair_size': 0.1,
    'interests': 0.3,
    'education': 0.1,
    'career': 0.05,
    'religion': 0.5,
    'description': 0.1
}

# Calculate compatibility for multiple users
results = calculate_compatibility_for_multiple_users(main_user, main_user_prefs, other_users, other_users_prefs, weights)
for user_id, compatibility in results:
    print(f"Compatibility with user {user_id}: {compatibility:.2f}%")
