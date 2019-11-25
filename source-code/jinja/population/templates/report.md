# Report

| person ID | year of birth | number of friends |
|-----------|---------------|-------------------|
{% for person in people %}
| {{ '%-9s'|format(person['id']) }} | {{ '%13d'|format(person['birthyear']) }} | {{ '%17d'|format(person['nr_friends']) }} |
{% endfor %}
