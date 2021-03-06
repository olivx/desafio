$(function(){


    function loadJobForm(){
         var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'GET',
            dataType: 'json',
            beforeSend: function(){
                $('#job-modal').modal('show');
            },
            success: function(data){
                $('#job-modal .modal-content').html(data.html_form);

                if(data.disable_all){
                    $('#job-modal input').attr('disabled','disabled');
                    $('#job-modal textarea').attr('disabled','disabled');
                    $('#job-modal select').attr('disabled','disabled');
                    $('#job-modal input[name=csrfmiddlewaretoken]').removeAttr('disabled');
                }
            }
        });
    };

    function saveJobForm(){
        var form =  $(this);
        $.ajax({
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            dataType: 'json',
            success: function(data){
                if(data.is_form_valid){

                    $('.job-table tbody').html(data.html_table);
                    $('.messages').html(data.message)
                    $('#job-modal').modal('hide');

                }else{
                    $('#job-modal .modal-content').html(data.html_form);
                    }
                }
        });
    return false;
    };

    function deleteJobForm(){
        var form =  $(this);
            $.ajax({
                url:  form.attr('action'),
                type: form.attr('method'),
                data: form.serialize(),
                dataType: 'json',
                beforeSend:function(){

                    var x = confirm('Você realmente deseja desativar esse cliente ?')
                    if (x == false){
                        return false;
                    }

                },
                success: function(data){
                    if(data.is_form_valid){

                        $('.job-table tbody').html(data.html_table);
                        $('.messages').html(data.message)
                        $('#job-modal').modal('hide');

                    }else{
                        $('#job-modal .modal-content').html(data.html_form);
                    }
                }
        });
    return false;
    };

    // save job
    $('.js-open-job-form').click(loadJobForm);
    $('#job-modal').on('submit', '.js-save-job-form', saveJobForm);

    // update job
    $('.job-table').on('click','button', loadJobForm);
    $('#job-modal').on('submit', '.js-update-job-form', saveJobForm);

    // delete job
    $('#job-modal').on('submit', '.js-delete-job-form', deleteJobForm);


    // detail job
     $('.js-open-job-form-detail').click(loadJobForm);




    // company  methods
    function loadCompanyForm(){
        var btn =  $(this);
        $.ajax({
            url:        btn.attr('data-url'),
            type:       'GET',
            dataType:   'json',

            beforeSend: function(){
                $('#company-modal').modal('show');
            },
            success: function(data){
                $('#company-modal .modal-content').html(data.html_form);
                if(data.disable_all){

                    $('input').attr('disabled', 'disabled')
                    $('textarea').attr('disabled', 'disabled')
                    $('select').attr('disabled', 'disabled')
                    $('#modal .btn-primary').attr('disabled', 'disabled')
                    $('input[name=csrfmiddlewaretoken]').removeAttr('disabled')


                }
            }
        });
    };

    function saveCompanyForm(){
        var form = $(this);
        $.ajax({
            dataType: 'json',
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),

            success: function(data){
                if(data.is_form_valid){
                     $('#company-table tbody').html(data.html_table);
                    $('.messages').html(data.message);
                    $('#company-modal').modal('hide');


                }else{

                    $('#company-modal .modal-content').html(data.html_form);
                }
            }
        });
    return false;
    };

    function deleteCompanyForm(){
        var form = $(this);
        $.ajax({

            dataType:'json',
            data: form.serialize(),
            url: form.attr('action'),
            type: 'post',

            beforeSend: function(){
                var x = confirm('Voce realmente deseja deletar essa Empresa ?')
                if(x == false){
                    return false;
                }
            },
            success: function(data){
                $('#company-table tbody').html(data.html_table);
                $('.pagination').html(data.html_pagination)
                $('#company-modal').modal('hide');
                $('.messages').html(data.message);

            }

        });
     return false;
    };

    // save company
    $('.js-open-company-form').click(loadCompanyForm);
    $('#company-modal').on('submit', '.js-save-company-form', saveCompanyForm);

    // update company
    $('#company-table').on('click', '.js-open-company-form-update', loadCompanyForm);
    $('#company-modal').on('submit', '.js-company-form-update', saveCompanyForm);

    // delete company
    $('#company-table').on('click' , '.js-open-company-form-delete', loadCompanyForm);
    $('#company-modal').on('submit', '.js-company-form-delete', deleteCompanyForm);


    // method address
    function busca_cep(){

        var cep =  $('.input_cep').val();
        cep  = cep.replace('-', '')
        var validacep = /^[0-9]{8}$/;

       // para ceps validos
        if(validacep.test(cep)){

            $.getJSON("http://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                if (!("erro" in dados)) {

                    $('#id_cep').mask('00000-000');

                    // update endereco
                    $('#id_endereco').val(dados.logradouro);
                    $('#id_bairro').val(dados.bairro);
                    $('#id_cidade').val(dados.localidade);
                    $('#id_uf').val(dados.uf);
                }
                else {
                    //CEP pesquisado não foi encontrado.
                    alert("CEP não encontrado.");
                }
            }); // get json

        }// valida cep
        else{

            alert('CEP invalido. \nverifique o campo CEP.')
        }


    }

    $('#modal-endereco').on('click','.search_cep', busca_cep)
    $('.search_cep').click(busca_cep)


    // limpa o modal de endereço
    $('.form_cleaned').click( function(){
             $.each($('input'),function(){
                $(this).val('');
            });

            $('textarea').val('');

    });


    // company methods endereco

    function submit_form_address_company(e){
            e.preventDefault();
            $("#company_id").removeAttr('disabled');
            var url = $(this).attr('data-url')
            $('#form_address').attr('action', url)
            $('#form_address').submit()
    }
    $('.js-save-address-form').click(submit_form_address_company);
    $('.js-update-address-form').click(submit_form_address_company);
    $('.js-delete-modal-address').click(function(e){
            e.preventDefault();

            var con = confirm('Desejan realmente deletar esse endereço ?')
            if(con == false){
                return false;
            }
            $("#company_id").removeAttr('disabled');
            var url = $(this).attr('data-url')
            $('#form_address').attr('action', url)
            $('#form_address').submit()
    });


     //perfil endereço methods

    function loadFormAddress(e){

        var btn = $(this);
        $.ajax({

            type: 'get',
            dataType: 'json',
            url: btn.attr('data-url'),

            beforeSend: function(){
                $('#modal-endereco').modal('show')
            },
            success: function(data){
                $('#modal-endereco .modal-content').html(data.html_form)
                if(data.disable_all){
                    $('#modal-endereco input').attr('disabled',true)
                    $('#modal-endereco textarea').attr('disabled',true)
                    $('#modal-endereco input[type=hidden]').removeAttr('disabled')
                }
            }

        });

    };

    function saveFormAddress(){
        var form = $(this);
        $.ajax({
            dataType: 'json',
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(data){

                if(data.is_form_valid){
                $('#modal-endereco').modal('hide')
                $('.messages').html(data.messages)
                $('.address_unicode').text(data.address)
                }else{
                  $('#modal-endereco .modal-content').html(data.html_form)
                }
            }
        });

    return false;
    }

    $('.js-open-address-form').click(loadFormAddress);
    $('#modal-endereco').on('submit', '.js-save-address-form', saveFormAddress);
    $('#modal-endereco').on('submit', '.js-update-address-form', saveFormAddress);
    $('#modal-endereco').on('submit', '.js-delete-address-form' , function(){
           var form = $(this)
            $.ajax({
            dataType: 'json',
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(data){

                if(data.is_form_valid){
                $('#modal-endereco').modal('hide')
                $('.messages').html(data.messages)
                $('.address_unicode').text(data.address)
                }else{
                  $('#modal-endereco .modal-content').html(data.html_form)
                }
            }
        });

    return false;
    });






    // subimit candaidate form
    function submit_form_candidate_save(e){
            e.preventDefault();
            var url = $(this).attr('data-url')
            $('.form_candidate').attr('action', url)
            $('.form_candidate').submit()
    };

    function submit_form_candidate_delete(e){
            var c = confirm('Deseja realmente deletar essas informações ?')

            if(c == true){
                e.preventDefault();
                var url = $(this).attr('data-url')
                $('.form_candidate').attr('action', url)
                $('.form_candidate').submit()
            }
    };

    $('.js-send-form-candidate-save').click(submit_form_candidate_save)
    $('.js-send-form-candidate-delete').click(submit_form_candidate_delete)


    //candidato
    function loadCandidatoForm(){
        var btn =  $(this);
        $.ajax({
            url:        btn.attr('data-url'),
            type:       'GET',
            dataType:   'json',

            beforeSend: function(){
                $('#candidato-modal').modal('show');
            },
            success: function(data){
                $('#candidato-modal .modal-content').html(data.html_form);
                if(data.disable_all){

                    $('input').attr('disabled', 'disabled')
                    $('textarea').attr('disabled', 'disabled')
                    $('select').attr('disabled', 'disabled')
                    $('#modal .btn-primary').attr('disabled', 'disabled')
                    $('input[name=csrfmiddlewaretoken]').removeAttr('disabled')


                }
            }
        });
    };

    function saveCompanyForm(){
        var form = $(this);
        $.ajax({
            dataType: 'json',
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),

            success: function(data){
                if(data.is_form_valid){
                     $('#company-table tbody').html(data.html_table);
                    $('.messages').html(data.message);
                    $('#company-modal').modal('hide');


                }else{

                    $('#company-modal .modal-content').html(data.html_form);
                }
            }
        });
    return false;
    };

    function deleteCompanyForm(){
        var form = $(this);
        $.ajax({

            dataType:'json',
            data: form.serialize(),
            url: form.attr('action'),
            type: 'post',

            beforeSend: function(){
                var x = confirm('Voce realmente deseja deletar essa Empresa ?')
                if(x == false){
                    return false;
                }
            },
            success: function(data){
                $('#company-table tbody').html(data.html_table);
                $('.pagination').html(data.html_pagination)
                $('#company-modal').modal('hide');
                $('.messages').html(data.message);

            }

        });
     return false;
    };

    $('#candidato-table').on('click', '.js-open-candidato-form-update', loadCandidatoForm);

    $('#modal-group').on('shown.bs.modal', function(){
        $('.modal .modal-body').css('overflow-y','auto');
        $('.modal .modal-body').css('height' , $(window).height() * 0.7 );
    });

    $('#modal-group').on('hidden.bs.modal', function () {
        $('#modal-product').modal('show');

        $.ajax({
            url: 'api/product/group/list/',
            dataType: 'json',

            success: function(data){

                 var json_obj = $.parseJSON(data.groups);
                 if(json_obj ){
                    $('select[name=group] option').remove();
                   // <option value="" selected="selected">---------</option>
                    $('select[name=group]').append($('<option>').text('---------').
                    attr('selected','selected').attr('value',''));
                 }
                 $.each(json_obj, function(key, obj){
                      $('select[name=group]').append($('<option>').text(obj.fields.group).attr('value', obj.pk));

                 });

            }

        });
    });

     $('#profile-detail').click(function(e){
            e.preventDefault();
            var a = $(this)

            $.ajax({
            url:        a.attr('href'),
            type:       'GET',
            dataType:   'json',

            beforeSend: function(){

                $('#candidato-modal').modal('show')

            },

            success: function(data){
                $('#candidato-modal .modal-content').html(data.html_form);
                $('#candidato-modal .modal-content .distancia .status').html(data.distancia.status);
            }
        });
    });

    // metodos de canidatos a um job de uma empresa

//    function JobCompanyProfileCandidateLoad(){
//
//        var btn = $(this)
//        $.ajax({
//             url:        btn.attr('data-url'),
//            type:       'GET',
//            dataType:   'json',
//
//            beforeSend: function(){
//                $('#candidate-modal').modal('show')
//            },
//            success: function(data){
//                $('#candidate-modal .modal-content').html(data.html_form)
//            }
//        });
//    }
//
//    $('.js-open-candidate-form-detail').click(JobCompanyProfileCandidateLoad)

});