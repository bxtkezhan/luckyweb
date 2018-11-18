{% if args.display_num %}
<h{{ args.head_num }} class="display-{{ args.display_num }}" >{{ args.text }}</h{{ args.head_num }}>
{% else %}
<h{{ args.head_num }} class="" >{{ args.text }}</h{{ args.head_num }}>
{% endif %}
