from django.contrib import messages
from django.shortcuts import render


def profile_save(request,obej_send, obje, Form_send, Form,
                 context_send, _context, msg_success,
                 template='jobauth/candidate_profile.html'):
    """
    
    :param request: 
    :param obej_send: 
    :param obje: 
    :param Form_send: 
    :param Form: 
    :param context_send: 
    :param _context: 
    :param msg_success: 
    :param template: 
    :return: 
    """

    send_form = Form_send(request.POST, instance=obej_send)

    _form = Form(instance=obje)
    if request.method == 'POST':

        if send_form.is_valid():
            obj = send_form.save(commit=False)
            obj.user = request.user
            obj.save()
            msg_success.encode('utf-8')
            messages.success(request, msg_success)
        else:
            msg_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msg_error)
            context = {
                context_send: send_form,
                _context: _form
            }
            return render(request, template, context)
    else:
        context = {
            context_send: send_form,
            _context: _form
        }
    return render(request, template, context)
