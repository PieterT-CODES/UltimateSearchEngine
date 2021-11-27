from django.shortcuts import render
import webbrowser as wb

def index(request):
    if 'boxs' in request.POST:
        result = request.POST['boxs']

        wb.open(f"https://www.ask.com/web?q={result}")
        wb.open(f"https://www.bing.com/search?q={result}")
        wb.open(f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={result}")
        wb.open(f"https://duckduckgo.com/?q={result}")
        wb.open(f"https://yandex.com/search/?text={result}")
        wb.open(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={result}")
        wb.open(f"https://search.aol.com/aol/search?q={result}")
        wb.open(f"https://gibiru.com/results.html?q={result}")
        wb.open(f"https://swisscows.com/web?query={result}")
        wb.open(f"https://www.ecosia.org/search?q={result}")
        wb.open(f"https://www.gigablast.com/search?c=main&qlangcountry=en-us&q={result}")
        wb.open(f"https://search18.lycos.com/web/?q={result}")
        wb.open(f"https://metager.org/meta/meta.ger3?eingabe={result}")
        wb.open(f"https://www.qwant.com/?l=en&q={result}")
    else: 
        result = False    

    return render(request, 'searchengine/index.html')