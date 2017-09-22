from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages

from core.utils import paginator


def view_service(request, object, Form, klass, template_name, context_list,
                 template_table, message_success, message_type='success', message_error=
                 'Foi encontrado algo errado no processo, corrija os erros a '
                 'baixo no formulario e tente novamente'):
    """
    :param request: 
    :param object: objeto que sera usado , company, job  
    :param Form:   formulario que deve ser chamdo
    :param klass:  classe que sera usado no klass.objects.all()
    :param template_name: template que sera renderesido no modal
    :param context_list: nome do context para lista de objetos
    :param template_table: nome do template da tabela que sera renderizado
    :param message_success: messagem de sucesso 
    :param message_type: messagem de sucesso update 
    :param message_error: messagem de erro
    :return: json com is_form_valid , html_table,  html_form
    """
    data = {}
    form = Form(request.POST or None, instance=object)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['is_form_valid'] = True
            companies = paginator(request, klass.objects.all())
            data['html_table'] = \
                render_to_string(template_table, {context_list: companies}, request=request)

            message = message_success
            if message_type == 'success':
                messages.success(request, message)
            else:
                messages.warning(request, message)
            data['message'] = render_to_string('core/messages.html', {}, request=request)

        else:
            data['is_form_valid'] = False
            message = message_error
            messages.error(request, message)
            data['message'] = render_to_string('core/messages.html', {}, request=request)
            data['html_form'] = \
                render_to_string(template_name, {'form': form}, request=request)
    else:
        data['html_form'] = \
            render_to_string(template_name, {'form': form}, request=request)

    return JsonResponse(data)
