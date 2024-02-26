-- website: https://www.google.com/

function main(splash, args)
  -- Setting the url
  url = args.url
  -- Go to the url and then wait 2 seconds to let the page render correctly
  assert(splash:go(url))
  assert(splash:wait(2))
  -- Return the HTML and a screenshot
  return {
    html = splash:html(),
    png = splash:png(),
  }
end