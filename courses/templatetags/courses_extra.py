__author__ = 'om'
from django import template
from courses.models import Course
import markdown2
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def newest_course():
    """ get the recent course that was added to library. """
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/courses_nav.html')
def nav_courses_list():
    """Return the dictionary of courses to create a navigation """
    courses = Course.objects.all()
    return {'courses': courses}

#register.inclusion_tag('courses/courses_nav.html')(nav_courses_list)

@register.filter('time_estimate')
def time_estimate(word_count):
    minutes = round(word_count/20)
    return minutes

@register.filter('mark_down_html')
def mark_down_html(markdown_text):
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
