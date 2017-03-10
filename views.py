#coding=utf-8
'''
Author:yuzg667
https://github.com/yuzg667/django_python_json_analysis
'''


import json
def py_json(request):
    
    if request.POST:
        form_commit = request.POST['q']
        if form_commit:
            try:
                js = json.loads(form_commit)
                json.dumps(js)
                message = json.dumps(js,indent=3,ensure_ascii=False)
                #�±��������Ҳ����
                # loads=demjson.decode(form_commit)
                # message=json.dumps(loads, indent=3, sort_keys=False, ensure_ascii=False)
            except Exception:
                 message = '���ύ��json��ʽ����ȷŶ~'

        else: 
            form_commit = u'''    {
                                "Json����":"�������json�ɣ�",
                                "��������tools":"ϲ�����ղء������"
                                }'''
            message = u'���������json�����~'

    else:
        form_commit = u'''      {
                                "Json����":"�������json�ɣ�",
                                "��������tools":"ϲ�����ղء������"
                                }'''
        message = u'����������jsonŶ~'

    #return render(request, 'tools/pyjson.html',ctx)
    return render(request, 'tools/pyjson.html',{'message':message, 
                                                'form_commit':form_commit,


                                                            })
