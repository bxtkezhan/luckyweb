{% if display_num %}
<h{{ head_num }} class="display-{{ display_num }}" >{{ text }}</h{{ head_num }}>
{% endif %}
{% if display_num|not %}
<h{{ head_num }} class="" >{{ text }}</h{{ head_num }}>
{% endif %}
