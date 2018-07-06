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
                #下边这个方法也可以
                # loads=demjson.decode(form_commit)
                # message=json.dumps(loads, indent=3, sort_keys=False, ensure_ascii=False)
            except Exception:
                 message = '您提交的json格式不正确哦~'

        else: 
            form_commit = u'''    {
                                "Json解析":"输入你的json吧！",
                                "人云亦云tools":"喜欢就收藏、分享吧"
                                }'''
            message = u'请输入你的json代码吧~'

    else:
        form_commit = u'''      {
                                "Json解析":"输入你的json吧！",
                                "人云亦云tools":"喜欢就收藏、分享吧"
                                }'''
        message = u'左侧框内输入json哦~'

    #return render(request, 'tools/pyjson.html',ctx)
    return render(request, 'tools/pyjson.html',{'message':message, 
                                                'form_commit':form_commit,
                                                            })
