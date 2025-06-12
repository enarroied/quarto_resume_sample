def create_star_rating(rating: float, max_rating: int = 5) -> str:
    """Create divs to represent rating as stars.

    Args:
        rating: The current rating (e.g., 3.5)
        max_rating: Maximum possible rating (default 5)

    Returns:
        HTML string with star rating display
    """
    full_stars = int(rating)
    has_half_star = (rating - full_stars) >= 0.5
    empty_stars = max_rating - full_stars - (1 if has_half_star else 0)

    stars_html = []

    # Add full stars
    for _ in range(full_stars):
        stars_html.append('<span style="color: gold;">★</span>')

    # Add half star if needed
    if has_half_star:
        stars_html.append('<span style="color: gold;">⯪</span>')

    # Add empty stars
    for _ in range(empty_stars):
        stars_html.append('<span style="color: grey;">☆</span>')

    return f'<div style="font-size: 10px; white-space: nowrap;">{"".join(stars_html)}</div>'
