from django import template

register = template.Library()

@register.filter(name="precio_clp")
def precio_clp(valor):
    try:
        numero = int(valor)
        return f"{numero:,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor
