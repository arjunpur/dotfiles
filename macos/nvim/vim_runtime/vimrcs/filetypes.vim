""""""""""""""""""""""""""""""
" => Python section
""""""""""""""""""""""""""""""
let python_highlight_all = 1
au FileType python syn keyword pythonDecorator True None False self

au BufNewFile,BufRead *.jinja set syntax=htmljinja
au BufNewFile,BufRead *.mako set ft=mako

au FileType python map <buffer> F :set foldmethod=indent<cr>

au FileType python inoremap <buffer> $r return 
au FileType python inoremap <buffer> $i import 
au FileType python inoremap <buffer> $p print 
au FileType python inoremap <buffer> $f #--- <esc>a
au FileType python map <buffer> <leader>1 /class 
au FileType python map <buffer> <leader>2 /def 
au FileType python map <buffer> <leader>C ?class 
au FileType python map <buffer> <leader>D ?def 
au FileType python set cindent
au FileType python set cinkeys-=0#
au FileType python set indentkeys-=0#


""""""""""""""""""""""""""""""
" => JavaScript section
"""""""""""""""""""""""""""""""
" au FileType javascript call JavaScriptFold()
au FileType javascript setl fen
" au FileType javascript setl nocindent
au FileType javascript setlocal sw=2
au FileType javascript setlocal ts=2
au FileType javascript setlocal sts=2

au FileType javascript imap <c-t> $log();<esc>hi
au FileType javascript imap <c-a> alert();<esc>hi

autocmd FileType typescript set cino+=(0


au FileType javascript inoremap <buffer> $r return 
au FileType javascript inoremap <buffer> $f //--- PH<esc>FP2xi

function! JavaScriptFold() 
    setl foldmethod=syntax
    setl foldlevelstart=1
    syn region foldBraces start=/{/ end=/}/ transparent fold keepend extend

    function! FoldText()
        return substitute(getline(v:foldstart), '{.*', '{...}', '')
    endfunction
    setl foldtext=FoldText()
endfunction


""""""""""""""""""""""""""""""
" => Typescript section
"""""""""""""""""""""""""""""""

au FileType typescript setlocal sw=2
au FileType typescript setlocal ts=2
au FileType typescript setlocal sts=2
autocmd FileType typescript nmap <buffer> <Leader><Leader>t : <C-u>echo tsuquyomi#hint()<CR>

""""""""""""""""""""""""""""""
" => React section
"""""""""""""""""""""""""""""""
autocmd BufNewFile,BufRead *.tsx,*.jsx set filetype=typescriptreact


""""""""""""""""""""""""""""""
" => CoffeeScript section
"""""""""""""""""""""""""""""""
function! CoffeeScriptFold()
    setl foldmethod=indent
    setl foldlevelstart=1
endfunction
au FileType coffee call CoffeeScriptFold()

au FileType gitcommit call setpos('.', [0, 1, 1, 0])


""""""""""""""""""""""""""""""
" => Shell section
""""""""""""""""""""""""""""""
au FileType sh setlocal sw=2
au FileType sh setlocal ts=2
au FileType sh setlocal sts=2

" if exists('$TMUX') 
"     if has('nvim')
"         set termguicolors
"     else
"         set term=screen-256color 
"     endif
" endif


""""""""""""""""""""""""""""""
" => Twig section
""""""""""""""""""""""""""""""
autocmd BufRead *.twig set syntax=html filetype=html

""""""""""""""""""""""""""""""
" => YAML
""""""""""""""""""""""""""""""
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

autocmd BufRead *.Jenkinsfile setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType groovy setlocal ts=2 sts=2 sw=2 expandtab

""""""""""""""""""""""""""""""
" => Golang 
""""""""""""""""""""""""""""""
let g:go_highlight_functions = 1
let g:go_highlight_function_calls = 1
let g:go_def_mode = 'gopls'
let g:go_info_mode='gopls'
" disable vim-go :GoDef short cut (gd)
" this is handled by LanguageClient [LC]
let g:go_def_mapping_enabled = 0
let g:go_code_completion_enabled = 0
let g:go_fmt_autosave = 1
let g:go_doc_keywordprg_enabled = 0
